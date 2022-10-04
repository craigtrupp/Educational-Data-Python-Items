<center>
    <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Access DB2 on Cloud using Python

Estimated time needed: **15** minutes

## Objectives

After completing this lab you will be able to:

*   Create a table
*   Insert data into the table
*   Query data from the table
*   Retrieve the result set into a pandas dataframe
*   Close the database connection


**Notice:** Please follow the instructions given in the first Lab of this course to Create a database service instance of Db2 on Cloud.

## Task 1: Import the `ibm_db` Python library

The `ibm_db` [API ](https://pypi.python.org/pypi/ibm_db/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01) provides a variety of useful Python functions for accessing and manipulating data in an IBM® data server database, including functions for connecting to a database, preparing and issuing SQL statements, fetching rows from result sets, calling stored procedures, committing and rolling back transactions, handling errors, and retrieving metadata.

We import the ibm_db library into our Python Application

The following required modules are pre-installed in the Skills Network Labs environment. However if you run this notebook commands in a different Jupyter environment (e.g. Watson Studio or Ananconda) you may need to install these libraries by removing the `#` sign before `!pip` in the code cell below.



```python
# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql
```


```python
import ibm_db
```

When the command above completes, the `ibm_db` library is loaded in your notebook.

## Task 2: Identify the database connection credentials

Connecting to dashDB or DB2 database requires the following information:

*   Driver Name
*   Database name
*   Host DNS name or IP address
*   Host port
*   Connection protocol
*   User ID
*   User Password

**Notice:** To obtain credentials please refer to the instructions given in the first Lab of this course

Now enter your database credentials below

Replace the placeholder values in angular brackets <> below with your actual database credentials

e.g. replace "database" with "BLUDB"



```python
#Replace the placeholder values with the actuals for your Db2 Service Credentials
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "****"            # e.g. "BLUDB"
dsn_hostname = "******"
dsn_port = "*****"                    # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "******"                 # e.g. "abc12345"
dsn_pwd = "*******"                 # e.g. "7dBZ3wWt9XN6$o0J"
dsn_security = "SSL"              #i.e. "SSL"
```

## Task 3: Create the database connection

Ibm_db API uses the IBM Data Server Driver for ODBC and CLI APIs to connect to IBM DB2 and Informix.

Create the database connection



```python
#Create database connection
#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

```

    Connected to database:  bludb as user:  **** on host:  1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud


## Task 4: Create a table in the database

In this step we will create a table in the database with following details:

<img src = "https://ibm.box.com/shared/static/ztd2cn4xkdoj5erlk4hhng39kbp63s1h.jpg" align="center">



```python
#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statment
dropStmt = ibm_db.exec_immediate(conn, dropQuery)
```

## Dont worry if you get this error:

If you see an exception/error similar to the following, indicating that INSTRUCTOR is an undefined name, that's okay. It just implies that the INSTRUCTOR table does not exist in the table - which would be the case if you had not created it previously.

Exception: \[IBM]\[CLI Driver]\[DB2/LINUXX8664] SQL0204N  "ABC12345.INSTRUCTOR" is an undefined name.  SQLSTATE=42704 SQLCODE=-204



```python
#Construct the Create Table DDL statement - replace the ... with rest of the statement
createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"

#Now fill in the name of the method and execute the statement
createStmt = ibm_db.exec_immediate(conn, createQuery)
```

<details><summary>Click here for the solution</summary>

```python
createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"

createStmt = ibm_db.exec_immediate(conn,createQuery)
```

</details>


## Task 5: Insert data into the table

In this step we will insert some rows of data into the table.

The INSTRUCTOR table we created in the previous step contains 3 rows of data:

<img src="https://ibm.box.com/shared/static/j5yjassxefrjknivfpekj7698dqe4d8i.jpg" align="center">

We will start by inserting just the first row of data, i.e. for instructor Rav Ahuja



```python
#Construct the query - replace ... with the insert statement
insertQuery = "INSERT INTO INSTRUCTOR (ID, FNAME, LNAME, CITY, CCODE) VALUES (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)
```

<details><summary>Click here for the solution</summary>

```python
insertQuery = "insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"

insertStmt = ibm_db.exec_immediate(conn, insertQuery)
```

</details>


Now use a single query to insert the remaining two rows of data



```python
#replace ... with the insert statement that inerts the remaining two rows of data
insertQuery2 = "INSERT INTO INSTRUCTOR (ID, FNAME, LNAME, CITY, CCODE) VALUES (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"

#execute the statement
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)
```

<details><summary>Click here for the solution</summary>

```python
insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"

insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)

```

</details>


## Task 6: Query data in the table

In this step we will retrieve data we inserted into the INSTRUCTOR table.



```python
#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

#Fetch the Dictionary (for the first row only) - replace ... with your code
# https://www.ibm.com/docs/en/db2/10.5?topic=db-fetching-rows-columns-from-result-sets
print(selectStmt)
print([method_name for method_name in dir(ibm_db)], '\n')
# print(ibm_db.fetch_tuple(selectStmt), 'Result set for fetch_tuple call off ibm_db API')
# print(ibm_db.fetch_assoc(selectStmt), 'Return for fetch_assoc call')
print(ibm_db.fetch_both(selectStmt), 'Return for fetch_both call')

    
```

    <ibm_db.IBM_DBStatement object at 0x7f545ce3d420>
    ['ATTR_CASE', 'CASE_LOWER', 'CASE_NATURAL', 'CASE_UPPER', 'IBM_DBClientInfo', 'IBM_DBConnection', 'IBM_DBServerInfo', 'IBM_DBStatement', 'PARAM_FILE', 'QUOTED_LITERAL_REPLACEMENT_OFF', 'QUOTED_LITERAL_REPLACEMENT_ON', 'SQL_API_SQLROWCOUNT', 'SQL_ATTR_AUTOCOMMIT', 'SQL_ATTR_CURRENT_SCHEMA', 'SQL_ATTR_CURSOR_TYPE', 'SQL_ATTR_INFO_ACCTSTR', 'SQL_ATTR_INFO_APPLNAME', 'SQL_ATTR_INFO_PROGRAMNAME', 'SQL_ATTR_INFO_USERID', 'SQL_ATTR_INFO_WRKSTNNAME', 'SQL_ATTR_QUERY_TIMEOUT', 'SQL_ATTR_ROWCOUNT_PREFETCH', 'SQL_ATTR_TRUSTED_CONTEXT_PASSWORD', 'SQL_ATTR_TRUSTED_CONTEXT_USERID', 'SQL_ATTR_USE_TRUSTED_CONTEXT', 'SQL_AUTOCOMMIT_OFF', 'SQL_AUTOCOMMIT_ON', 'SQL_BIGINT', 'SQL_BINARY', 'SQL_BIT', 'SQL_BLOB', 'SQL_BLOB_LOCATOR', 'SQL_BOOLEAN', 'SQL_CHAR', 'SQL_CLOB', 'SQL_CLOB_LOCATOR', 'SQL_CURSOR_DYNAMIC', 'SQL_CURSOR_FORWARD_ONLY', 'SQL_CURSOR_KEYSET_DRIVEN', 'SQL_CURSOR_STATIC', 'SQL_DBCLOB', 'SQL_DBCLOB_LOCATOR', 'SQL_DBMS_NAME', 'SQL_DBMS_VER', 'SQL_DECFLOAT', 'SQL_DECIMAL', 'SQL_DOUBLE', 'SQL_FALSE', 'SQL_FLOAT', 'SQL_GRAPHIC', 'SQL_INDEX_CLUSTERED', 'SQL_INDEX_OTHER', 'SQL_INTEGER', 'SQL_LONGVARBINARY', 'SQL_LONGVARCHAR', 'SQL_LONGVARGRAPHIC', 'SQL_NUMERIC', 'SQL_PARAM_INPUT', 'SQL_PARAM_INPUT_OUTPUT', 'SQL_PARAM_OUTPUT', 'SQL_REAL', 'SQL_ROWCOUNT_PREFETCH_OFF', 'SQL_ROWCOUNT_PREFETCH_ON', 'SQL_SMALLINT', 'SQL_TABLE_STAT', 'SQL_TINYINT', 'SQL_TRUE', 'SQL_TYPE_DATE', 'SQL_TYPE_TIME', 'SQL_TYPE_TIMESTAMP', 'SQL_VARBINARY', 'SQL_VARCHAR', 'SQL_VARGRAPHIC', 'SQL_WCHAR', 'SQL_WLONGVARCHAR', 'SQL_WVARCHAR', 'SQL_XML', 'USE_WCHAR', 'WCHAR_NO', 'WCHAR_YES', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'active', 'autocommit', 'bind_param', 'callproc', 'check_function_support', 'client_info', 'close', 'column_privileges', 'columns', 'commit', 'conn_error', 'conn_errormsg', 'conn_warn', 'connect', 'createdb', 'createdbNX', 'cursor_type', 'dropdb', 'exec_immediate', 'execute', 'execute_many', 'fetch_assoc', 'fetch_both', 'fetch_row', 'fetch_tuple', 'field_display_size', 'field_name', 'field_nullable', 'field_num', 'field_precision', 'field_scale', 'field_type', 'field_width', 'foreign_keys', 'free_result', 'free_stmt', 'get_db_info', 'get_last_serial_value', 'get_num_result', 'get_option', 'next_result', 'num_fields', 'num_rows', 'pconnect', 'prepare', 'primary_keys', 'procedure_columns', 'procedures', 'recreatedb', 'result', 'rollback', 'server_info', 'set_option', 'special_columns', 'statistics', 'stmt_error', 'stmt_errormsg', 'stmt_warn', 'table_privileges', 'tables'] 
    
    {'ID': 1, 0: 1, 'FNAME': 'Rav', 1: 'Rav', 'LNAME': 'Ahuja', 2: 'Ahuja', 'CITY': 'TORONTO', 3: 'TORONTO', 'CCODE': 'CA', 4: 'CA'} Return for fetch_both call


<details><summary>Click here for the solution</summary>

```python
#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

#Fetch the Dictionary (for the first row only)
ibm_db.fetch_both(selectStmt)

```

</details>



```python
#Fetch the rest of the rows and print the ID and FNAME for those rows (see how result has the column values available through index or Key name
while ibm_db.fetch_row(selectStmt) != False:
   print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))
```

     ID: 2  FNAME: Raul
     ID: 3  FNAME: Hima


<details><summary>Click here for the solution</summary>

```python
#Fetch the rest of the rows and print the ID and FNAME for those rows
while ibm_db.fetch_row(selectStmt) != False:
    print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))

```

</details>


Bonus: now write and execute an update statement that changes the Rav's CITY to MOOSETOWN



```python
#Enter your code below
update_Rav = "UPDATE INSTRUCTOR SET CITY='MOOSETOWN' WHERE FNAME='Rav'"
# Execute Update
updStmt = ibm_db.exec_immediate(conn, update_Rav)
```

<details><summary>Click here for the solution</summary>

```python
updateQuery = "update INSTRUCTOR set CITY='MOOSETOWN' where FNAME='Rav'"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

```

</details>


## Task 7: Retrieve data into Pandas

In this step we will retrieve the contents of the INSTRUCTOR table into a Pandas dataframe



```python
import pandas
import ibm_db_dbi
```


```python
#connection for pandas
pconn = ibm_db_dbi.Connection(conn)
```


```python
#query statement to retrieve all rows in INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#retrieve the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)

#print just the LNAME for first row in the pandas data frame and the last row's Fname, Lname, & City
print(pdf.LNAME[0], '\n', pdf.loc[pdf['LNAME'] == 'Vasudevan'][['FNAME', 'LNAME', 'CITY']])
```

    Ahuja 
       FNAME      LNAME     CITY
    2  Hima  Vasudevan  Chicago



```python
#print the entire data frame (Check Update Statement above for Rav City update) and update index to ID from table
pdf.set_index('ID', inplace=True)
print(pdf)
```

       FNAME      LNAME       CITY CCODE
    ID                                  
    1    Rav      Ahuja  MOOSETOWN    CA
    2   Raul      Chong    Markham    CA
    3   Hima  Vasudevan    Chicago    US


Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.

For example you can use the shape method to see how many rows and columns are in the dataframe



```python
pdf.shape
```




    (3, 4)



## Task 8: Close the Connection

We free all resources by closing the connection. Remember that it is always important to close connections so that we can avoid unused connections taking up resources.



```python
ibm_db.close(conn)
```




    True



## Summary

In this tutorial you established a connection to a database instance of DB2 Warehouse on Cloud from a Python notebook using ibm_db API. Then created a table and insert a few rows of data into it. Then queried the data. You also retrieved the data into a pandas dataframe.


## Author

<a href="https://www.linkedin.com/in/ravahuja/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01" target="_blank">Rav Ahuja</a>

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
| ----------------- | ------- | ---------- | ---------------------------------- |
| 2021-11-17        | 2.2     | Lakshmi    | Updated library                    |
| 2021-07-09        | 2.1     | Malika     | Updated connection string          |
| 2020-08-28        | 2.0     | Lavanya    | Moved lab to course repo in GitLab |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

