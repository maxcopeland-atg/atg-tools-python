# ATGDE Python Development Standard v0.1

TODO: Replace ATGDE Leadership with Python Steering Committee?

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
    kettle/
    sql/
    python/
        01_SFDCContract.py
        02_SFDCSubscription.py
        foobar_utils/
            __init__.py
            foobar_utils.py
```
Consider a data migration for a fictional client named "Foobar". 
All projects using python will have a root directory indicating client project name (see GitHub standards). Here, `foobar_migration/`.

Underneath the root directory contains a directory for each tool being used on the project. This separates technologies used 

## Script Scope and Naming Convention
The name of every ETL script--independent of technology-- should be concise and unambiguous as to functionality encapuslated therein. For transformation 

# Libraries
To ensure transferrability, Only ATGDE-approved libraries:
* All Python standard libraries (os, sys, csv, etc)
* Pandas
* sqlalchemy
* pyodbc
* simple_salesforce

Note: Exceptions can be made if projects or implementations require additional packages. Requests should be made to ATGDE leadership to vet package compliance.


# Style Guide
For sake of consistency and development best practices, any and all scripts must conform to the PEP8 style convention. (link)

It is strongly recommended that a PEP8 style checker be used by either an IDE or use `pycodestyle` via the command line.



