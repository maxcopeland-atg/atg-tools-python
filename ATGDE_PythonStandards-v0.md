# ATGDE Python Development Standard v0.1
author: Max Copeland (max.copeland@atginfo.com)

**Python** is a general-purpose programming language and has become the de-facto standard in Data Engineering tech stacks, being a required language profiency in over two-thirds of data engineering practices worldwide. Python's popularity lies in its simple syntax, readability, abundance of third-party libraries, and breadth of user base.

For our practice at ATG, Python, when written effectively, can serve most any technical requirement that may arise on an ETL project, and in many cases, can do so in a fraction of the development time required by using Kettle or SQL alone.

With the dynamic nature of our project work, the inclusion of Python to DE's tech stack depends on *transferrability*; i.e. Python scripts should be written in a way that is familiar to other Python-proficient engineers. A *transferrable* Python project should be able to have another engineer step in and continue development to completion with minimal Python-specific knowledge transfer.

To ensure the transferrability of any Python project, any and all ATG Data Engineers using Python must adhere and abide by the set of development standards as described in this document. 

## What this document is:
A set of strict standards surrounding Python development on billable data engineering project work. This set of standards is *not* a training document, nor a "how-to" guide for using Python on a project. (See training material).

## Who this document is for:
Any and all Data Engineers passing the **Python Proficiency Evaluation** and approved for Python use on billable data engineering project work.

### Python Proficiency Evaluation (PPE)
Any and all Data Engineers interested in using Python on billable data engineering project work must pass a one-time live Python evaluation to ensure syntatical and technical capacity to comply with the listed standards (Python built-in's, OOP principles, file I/O, pandas basic syntax, etc.).

# Project Structure
```
foobar_migration/
    sql/
    python/
        00_EXTRACT_SFDC.py
        01_TRANSFORM_SFDCContract.py
        02_TRANSFORM_SFDCSubscription.py
        foobar_utils/
            __init__.py
            foobar_utils.py
    kettle/
        03_LOAD_SFDCContract.py
        04_LOAD_SFDCSubscription.py
    data/
        input/
        output/
```
Consider a data migration for a fictional client named "Foobar". 
All projects using python will have a root directory indicating client project name (see GitHub standards). Here, `foobar_migration/`.

Underneath the root directory contains a directory for each tool being used on the project. 

## Script Scope and Naming Convention
Python scripts should be broken out in the following way:
* One script per Extract phase per datasource
* One script per Transformation per target object
* One script per Load phase per target object

The name of every ETL script--independent of technology-- should be concise and unambiguous as to functionality encapuslated therein. As such, each ETL script across all technologies used should be named with the following convention:

1. Prefixed with a two-digit number indicating order of execution, followed by an underscore.
2. Followed by ETL phase "EXTRACT", "TRANSFORM", or "LOAD", followed by an underscore.
3. Name of relevant datasource or target object.

    e.g. ` 01_TRANSFORM_SFDCContract.py`

It is strongly recommended that Python only be used for extracting and transforming project data, while loads be delegated to Kettle or FuseKit.

# Libraries
To ensure transferrability, Only ATGDE-approved libraries:
* All Python standard libraries (os, sys, csv, etc)
* Pandas (imported as `pd`)
* sqlalchemy
* pyodbc
* simple_salesforce

Note: Exceptions can be made if projects or implementations require additional packages. Requests should be made to ATGDE leadership to vet package compliance.

# pandas
The `pandas` will serve as the common framework for interfacing with relevant in-scope data. The `pandas` package stands as the de-facto transformation tool for most all data volumes on CPQ and/or Billing project work. This framework contains robust transformation functionality in a simple, intuitive interface that avoids having to write common transformations from scratch, keeping development time minimal.

All necessary datasets must be read as `pandas.Dataframe` objects and interfaced as such.


(pandas link)


# Style Guide
For sake of consistency and development best practices, any and all scripts must conform to the PEP8 style convention. (link)

It is strongly recommended that a PEP8 style checker be used by either an IDE or use `pycodestyle` via the command line.

# Functions
Each necessary transformation should be written in a function. Isolating each transformation into a single function allows for reusability and testability. 

The function name should be descriptive, abide by PEP8 standards, and be unambiguous as to the function purpose.

Each function must also have a docstring describing the functionality and requirements 
satisfied by the function, as well as a list of arguments and outputs for the function along with their respective datatypes.

Consider the following example of a simple transformation creating a custom field from an existing field on the in-scope data.

```
def annual_price_to_monthly(contracts_df):
    """
    Function to create a monthly_price column calculated from the 
    existing annual_price column.

    input
    -----
    contracts_df: pandas Dataframe object, Contract data pulled from Salesforce

    output
    -----
    None
    """

    contracts_df['monthly_price'] = contracts_df['annual_price'] / 12.0
```

Notice the function has no return statement. This function alters the dataframe passed to the function, as opposed to returning a copy of the dataframe. This convention is strongly recommended, as it avoids unnecessary memory allocation, and imporves readability of sequential transformations.

For testability, no two transformations should occur within the same function. In the event of a failed test, this avoids ambiguity around which transformation produces error.

# Script Execution
All transformations should be executed at the script level within the block `if __name__ == __main__:` after *all* of the function definitions.

e.g. in the following simple transformation sequence
```
if __name__ == __main__:
    
    # Reading contracts data extract to dataframe
    contracts_df = pd.read_csv("data/SFDC-Contract-Extract.csv')

    # Creating monthly price column
    annual_price_to_monthly(contracts_df)

    # Calcuating monthly discount from montly price
    calc_monthly_discount(contracts_df)

    # Writing transformed data to csv
    contracts_df.to_csv("data/SFDC-Contract-Transformed.csv)
```

# I/O and Data Staging
Data format for extracts and transformation outputs should be flat files *or* be staged in SQL, depending on developer preference and project requirements. 

# Python Script Reviews
All python scripts in active development should be regularly reviewed by senior DE to ensure standards compliance and to provide technical guidance and support.

As such, all DE's with python scripts in active development must attend the weekly python working group.