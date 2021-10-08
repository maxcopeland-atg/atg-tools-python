import pandas as pd
import pyodbc
from simple_salesforce import Salesforce
from sqlalchemy import create_engine
import urllib


def login_to_Salesforce(credentials):
    print('Connecting to Salesforce...')
    sf = Salesforce(
        username=credentials['Username'],
        password=credentials['Password'],
        security_token=credentials['Token'],
        domain=credentials['Domain']
    )
    return sf

def login_to_database(credentials):
    SERVER = '{},{}'.format(credentials['Server'], credentials['Port'])
    database = credentials['Name']
    # username = credentials['Username']
    # password = credentials['Password']

    print("Connecting to database...")
    # cnxn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + SERVER + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
    # cnxn = pyodbc.connect(Trusted_Connection='Yes',
    #                       Driver='DRIVER={ODBC Driver 17 for SQL Server};SERVER=',
    #                       Server=SERVER,
    #                       Database=database)

    # cnxn = pyodbc.connect(
    #     Trusted_Connection='Yes',
    #     Driver='{ODBC Driver 17 for SQL Server}',
    #     Server=SERVER,
    #     Database=database
    # )
    cnxn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + SERVER + ';DATABASE=' + database + ';Trusted_Connection=yes;'
    cnxn = pyodbc.connect(cnxn_str)

    quoted_cnxn_str = urllib.parse.quote_plus(cnxn_str)
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={quoted_cnxn_str}')

    return cnxn, engine
