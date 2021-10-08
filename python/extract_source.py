import argparse
import sys
import json

import pandas as pd
from tqdm import tqdm

from utils import utils


def get_sf_object_record_count(sf_instance, sf_object):
    obj_metadata = sf_instance.__getattr__(sf_object).describe()

    obj_name = obj_metadata['name']

    q = f'SELECT COUNT(Id) FROM {obj_name}'

    query = sf_instance.query(q)

    return query['records'][0]['expr0']


def get_all_data_soql_query(sf_instance, sf_object, filter_migrated = True, filter_unmigrated = False):
    """
    :param sf_instance:
    :param sf_object:
    :return:
    """
    if (filter_migrated and filter_unmigrated):
        raise ValueError("Setting filter_migrated and filter_unmigrated to True will return 0 records")


    obj_metadata = sf_instance.__getattr__(sf_object).describe()
    query = 'SELECT '

    for i, field in enumerate(obj_metadata['fields']):
        if i == len(obj_metadata['fields']) - 1:
            query += field['name']
        else:
            query += (field['name']) + ', '

    query += ' FROM {}'.format(obj_metadata['name'])

    if filter_migrated and 'Migrated_Record__c' in [field['name'] for field in obj_metadata['fields']]:
        query += ' WHERE Migrated_Record__c = false'

    elif filter_unmigrated and 'Migrated_Record__c' in [field['name'] for field in obj_metadata['fields']]:
        query += ' WHERE Migrated_Record__c = true'

    return query


def drop_problem_columns(df):
    """
    Utility to delete columns of dtype OrderedDict, to avoid breaking SQLAlchemy inserts
    :param df:
    :return:
    """
    # These fields contain OrderedDict types, and breaks sqlalchemy
    if 'attributes' in df.columns:
        del df['attributes']

    if 'BillingAddress' in df.columns:
        del df['BillingAddress']

    if 'ShippingAddress' in df.columns:
        del df['ShippingAddress']


def load_data_into_mssql(sf_instance, query, engine, table_name, record_count, schema='medidata_cpq'):
    """
    :param sf_instance:
    :param query:
    :param engine:
    :param table_name:
    :return:
    """

    with tqdm(total=record_count) as pbar:

        # sf_records = sf_instance.query_all(query)['records']

        # Make initial query of data
        initial_query = sf_instance.query(query)
        more_records = not initial_query['done']
        if more_records:
            next_records_url = initial_query['nextRecordsUrl']

        # Put records into pandas dataframe
        df = pd.DataFrame(initial_query['records']).convert_dtypes()
        drop_problem_columns(df)

        # Load data into database
        df.to_sql(table_name, con=engine, if_exists='replace', schema=schema)
        pbar.update(len(df))

        # Loop through data, appending to table
        while more_records:
            query = sf_instance.query_more(next_records_url, True)
            more_records = not query['done']
            try:
                next_records_url = query['nextRecordsUrl']
            except:
                more_records = False
            df = pd.DataFrame(query['records']).convert_dtypes()
            drop_problem_columns(df)

            df.to_sql(table_name, con=engine, if_exists='append', schema=schema)
            pbar.update(len(df))


if __name__ == "__main__":

    with open('../.secrets/credentials.json') as _file:
        credentials = json.load(_file)

    cnxn, engine = utils.login_to_database(credentials['Database'])

    sf_org_name = 'SIT'
    sf = utils.login_to_Salesforce(credentials['Salesforce'][sf_org_name])

    parser = argparse.ArgumentParser()

    parser.add_argument('sf_objects', type=str, nargs='+', help='SF Object API name(s)')

    args = parser.parse_args()

    for obj in args.sf_objects:
        record_count = get_sf_object_record_count(sf, obj)
        print(record_count)
        print('Loading {} Data...'.format(obj))


        soql_query = get_all_data_soql_query(sf, obj)

        load_data_into_mssql(sf, query=soql_query, engine=engine,
                             table_name='SFDC_{0}_{1}'.format(sf_org_name, obj), record_count=record_count)


