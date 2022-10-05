<center>
    <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Working with a real world data-set using SQL and Python

Estaimted time needed: **30** minutes

## Objectives

After complting this lab you will be able to:

*   Understand the dataset for Chicago Public School level performance
*   Store the dataset in an Db2 database on IBM Cloud instance
*   Retrieve metadata about tables and columns and query data from mixed case columns
*   Solve example problems to practice your SQL skills including using built-in database functions


## Chicago Public Schools - Progress Report Cards (2011-2012)

The city of Chicago released a dataset showing all school level performance data used to create School Report Cards for the 2011-2012 school year. The dataset is available from the Chicago Data Portal: [https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

This dataset includes a large number of metrics. Start by familiarizing yourself with the types of metrics in the database: [https://data.cityofchicago.org/api/assets/AAD41A13-BE8A-4E67-B1F5-86E711E09D5F?download=true](https://data.cityofchicago.org/api/assets/AAD41A13-BE8A-4E67-B1F5-86E711E09D5F?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01&download=true&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

**NOTE**:

Do not download the dataset directly from City of Chicago portal. Instead download a static copy which is a more database friendly version from this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01">link</a>.

**NOTE**:

For the learners who are encountering issues with loading from .csv in DB2 on Firefox, you can download the .txt files and load the data with those: <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.txt?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01">link</a>.

Now review some of its contents.


### Store the dataset in a Table

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. To analyze the data using SQL, it first needs to be stored in the database.

While it is easier to read the dataset into a Pandas dataframe and then PERSIST it into the database as we saw in the previous lab, it results in mapping to default datatypes which may not be optimal for SQL querying. For example a long textual field may map to a CLOB instead of a VARCHAR.

Therefore, **it is highly recommended to manually load the table using the database console LOAD tool, as indicated in Week 2 Lab 1 Part II**. The only difference with that lab is that in Step 5 of the instructions you will need to click on create "(+) New Table" and specify the name of the table you want to create and then click "Next".

##### Now open the Db2 console, open the LOAD tool, Select / Drag the .CSV file for the CHICAGO PUBLIC SCHOOLS dataset and load the dataset into a new table called **SCHOOLS**.

<a href="https://cognitiveclass.ai/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01"><img src = "https://ibm.box.com/shared/static/uc4xjh1uxcc78ks1i18v668simioz4es.jpg"></a>


### Connect to the database

Let us now load the ipython-sql  extension and establish a connection with the database

The following modules are pre-installed in the Skills Network Labs environment. However if you run this notebook commands in a different Jupyter environment (e.g. Watson Studio or Ananconda) you may need to install these libraries by removing the `#` sign before `!pip` in the code cell below.



```python
# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql
```


```python
%load_ext sql
```


```python
# Enter the connection string for your Db2 on Cloud database instance below
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL
%sql ibm_db_sa://cgv02624:**************@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb?security=SSL
```




    'Connected: cgv02624@bludb'



### Query the database system catalog to retrieve table metadata

##### You can verify that the table creation was successful by retrieving the list of all tables in your schema and checking whether the SCHOOLS table was created



```python
# type in your query to retrieve list of all tables in the database for your db2 schema (username)
%sql SELECT * FROM SYSCAT.TABLES LIMIT 5;

# Locate my tabschema
%sql SELECT DISTINCT(tabschema) FROM SYSCAT.TABLES;

%sql SELECT tabschema, tabname, owner, create_time FROM SYSCAT.TABLES WHERE tabschema = 'CGV02624';
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.
     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.
     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>tabschema</th>
            <th>tabname</th>
            <th>owner</th>
            <th>create_time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CGV02624</td>
            <td>INSTRUCTOR</td>
            <td>CGV02624</td>
            <td>2022-10-04 16:10:14.859290</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>INTERNATIONAL_STUDENT_TEST_SCORES</td>
            <td>CGV02624</td>
            <td>2022-10-04 17:14:56.572800</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>CHICAGO_SOCIOECONOMIC_DATA</td>
            <td>CGV02624</td>
            <td>2022-10-04 19:31:47.213436</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>SCHOOLS</td>
            <td>CGV02624</td>
            <td>2022-10-04 21:53:30.205989</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>EMPLOYEES</td>
            <td>CGV02624</td>
            <td>2022-10-02 15:58:42.046114</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>JOB_HISTORY</td>
            <td>CGV02624</td>
            <td>2022-10-02 15:58:42.251599</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>JOBS</td>
            <td>CGV02624</td>
            <td>2022-10-02 15:58:42.521359</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>DEPARTMENTS</td>
            <td>CGV02624</td>
            <td>2022-10-02 15:58:42.841020</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>LOCATIONS</td>
            <td>CGV02624</td>
            <td>2022-10-02 15:58:43.155223</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>PETRESCUE</td>
            <td>CGV02624</td>
            <td>2022-10-03 15:01:02.313081</td>
        </tr>
    </tbody>
</table>




```python
# \ Escape multi-line query with single magic %sql
%sql SELECT TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES \
      WHERE TABSCHEMA NOT IN ('SYSIBM', 'SYSCAT', 'SYSSTAT', 'SYSIBMADM', 'SYSTOOLS', 'SYSPUBLIC');
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>tabschema</th>
            <th>tabname</th>
            <th>create_time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CGV02624</td>
            <td>INSTRUCTOR</td>
            <td>2022-10-04 16:10:14.859290</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>INTERNATIONAL_STUDENT_TEST_SCORES</td>
            <td>2022-10-04 17:14:56.572800</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>CHICAGO_SOCIOECONOMIC_DATA</td>
            <td>2022-10-04 19:31:47.213436</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>SCHOOLS</td>
            <td>2022-10-04 21:53:30.205989</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>EMPLOYEES</td>
            <td>2022-10-02 15:58:42.046114</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>JOB_HISTORY</td>
            <td>2022-10-02 15:58:42.251599</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>JOBS</td>
            <td>2022-10-02 15:58:42.521359</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>DEPARTMENTS</td>
            <td>2022-10-02 15:58:42.841020</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>LOCATIONS</td>
            <td>2022-10-02 15:58:43.155223</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>PETRESCUE</td>
            <td>2022-10-03 15:01:02.313081</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
In Db2 the system catalog table called SYSCAT.TABLES contains the table metadata
-->


Double-click **here** for the solution.

<!-- Solution:

%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='YOUR-DB2-USERNAME'

or, you can retrieve list of all tables where the schema name is not one of the system created ones:

%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES \
      where TABSCHEMA not in ('SYSIBM', 'SYSCAT', 'SYSSTAT', 'SYSIBMADM', 'SYSTOOLS', 'SYSPUBLIC')
      
or, just query for a specifc table that you want to verify exists in the database
%sql select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'

-->


### Query the database system catalog to retrieve column metadata

##### The SCHOOLS table contains a large number of columns. How many columns does this table have?



```python
# type in your query to retrieve the number of columns in the SCHOOLS table
%sql SELECT COUNT(*) AS Column_Count_Schools \
     FROM SYSCAT.COLUMNS \
     WHERE tabname = 'SCHOOLS' AND tabschema = 'CGV02624' \
     LIMIT 3;

```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>column_count_schools</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>78</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
In Db2 the system catalog table called SYSCAT.COLUMNS contains the column metadata
-->


Double-click **here** for the solution.

<!-- Solution:

%sql select count(*) from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

-->


Now retrieve the the list of columns in SCHOOLS table and their column type (datatype) and length.



```python
# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length (Let's look at the columns return first)
%sql SELECT * FROM SYSCAT.COLUMNS WHERE tabname = 'SCHOOLS' and tabschema = 'CGV02624' LIMIT 3;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>tabschema</th>
            <th>tabname</th>
            <th>colname</th>
            <th>colno</th>
            <th>typeschema</th>
            <th>typename</th>
            <th>length</th>
            <th>scale</th>
            <th>typestringunits</th>
            <th>stringunitslength</th>
            <th>DEFAULT</th>
            <th>NULLS</th>
            <th>codepage</th>
            <th>collationschema</th>
            <th>collationname</th>
            <th>logged</th>
            <th>compact</th>
            <th>colcard</th>
            <th>high2key</th>
            <th>low2key</th>
            <th>avgcollen</th>
            <th>keyseq</th>
            <th>partkeyseq</th>
            <th>nquantiles</th>
            <th>nmostfreq</th>
            <th>numnulls</th>
            <th>target_typeschema</th>
            <th>target_typename</th>
            <th>scope_tabschema</th>
            <th>scope_tabname</th>
            <th>source_tabschema</th>
            <th>source_tabname</th>
            <th>dl_features</th>
            <th>special_props</th>
            <th>hidden</th>
            <th>inline_length</th>
            <th>pctinlined</th>
            <th>IDENTITY</th>
            <th>rowchangetimestamp</th>
            <th>GENERATED</th>
            <th>text</th>
            <th>compress</th>
            <th>avgdistinctperpage</th>
            <th>pagevarianceratio</th>
            <th>sub_count</th>
            <th>sub_delim_length</th>
            <th>avgcollenchar</th>
            <th>implicitvalue</th>
            <th>seclabelname</th>
            <th>rowbegin</th>
            <th>rowend</th>
            <th>transactionstartid</th>
            <th>pctencoded</th>
            <th>avgencodedcollen</th>
            <th>qualifier</th>
            <th>func_path</th>
            <th>randdistkey</th>
            <th>remarks</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CGV02624</td>
            <td>SCHOOLS</td>
            <td>10th Grade PLAN (2009)</td>
            <td>58</td>
            <td>SYSIBM  </td>
            <td>VARCHAR</td>
            <td>4</td>
            <td>0</td>
            <td>OCTETS</td>
            <td>4</td>
            <td>None</td>
            <td>Y</td>
            <td>1208</td>
            <td>SYSIBM</td>
            <td>IDENTITY</td>
            <td> </td>
            <td> </td>
            <td>45</td>
            <td>&#x27;24.5&#x27;</td>
            <td>&#x27;12.9&#x27;</td>
            <td>8</td>
            <td>None</td>
            <td>0</td>
            <td>-1</td>
            <td>-1</td>
            <td>0</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td> </td>
            <td>0</td>
            <td>-1</td>
            <td>N</td>
            <td>N</td>
            <td> </td>
            <td>None</td>
            <td>O</td>
            <td>None</td>
            <td>-1.0</td>
            <td>-1</td>
            <td>-1</td>
            <td>3</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>N</td>
            <td>N</td>
            <td>-1</td>
            <td>-1.0</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>None</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>SCHOOLS</td>
            <td>10th Grade PLAN (2010)</td>
            <td>59</td>
            <td>SYSIBM  </td>
            <td>VARCHAR</td>
            <td>4</td>
            <td>0</td>
            <td>OCTETS</td>
            <td>4</td>
            <td>None</td>
            <td>Y</td>
            <td>1208</td>
            <td>SYSIBM</td>
            <td>IDENTITY</td>
            <td> </td>
            <td> </td>
            <td>49</td>
            <td>&#x27;24.7&#x27;</td>
            <td>&#x27;12.7&#x27;</td>
            <td>8</td>
            <td>None</td>
            <td>0</td>
            <td>-1</td>
            <td>-1</td>
            <td>0</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td> </td>
            <td>0</td>
            <td>-1</td>
            <td>N</td>
            <td>N</td>
            <td> </td>
            <td>None</td>
            <td>O</td>
            <td>None</td>
            <td>-1.0</td>
            <td>-1</td>
            <td>-1</td>
            <td>3</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>N</td>
            <td>N</td>
            <td>-1</td>
            <td>-1.0</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>None</td>
        </tr>
        <tr>
            <td>CGV02624</td>
            <td>SCHOOLS</td>
            <td>11th Grade Average ACT (2011)</td>
            <td>61</td>
            <td>SYSIBM  </td>
            <td>VARCHAR</td>
            <td>4</td>
            <td>0</td>
            <td>OCTETS</td>
            <td>4</td>
            <td>None</td>
            <td>Y</td>
            <td>1208</td>
            <td>SYSIBM</td>
            <td>IDENTITY</td>
            <td> </td>
            <td> </td>
            <td>53</td>
            <td>&#x27;28.8&#x27;</td>
            <td>&#x27;13.6&#x27;</td>
            <td>8</td>
            <td>None</td>
            <td>0</td>
            <td>-1</td>
            <td>-1</td>
            <td>0</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td> </td>
            <td>0</td>
            <td>-1</td>
            <td>N</td>
            <td>N</td>
            <td> </td>
            <td>None</td>
            <td>O</td>
            <td>None</td>
            <td>-1.0</td>
            <td>-1</td>
            <td>-1</td>
            <td>3</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>N</td>
            <td>N</td>
            <td>-1</td>
            <td>-1.0</td>
            <td>None</td>
            <td>None</td>
            <td>N</td>
            <td>None</td>
        </tr>
    </tbody>
</table>




```python
# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
%sql SELECT colname, typename, length \
     FROM SYSCAT.COLUMNS \
     WHERE tabname = 'SCHOOLS' and tabschema = 'CGV02624';
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>colname</th>
            <th>typename</th>
            <th>length</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>10th Grade PLAN (2009)</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>10th Grade PLAN (2010)</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>11th Grade Average ACT (2011)</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>9th Grade EXPLORE (2009)</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>9th Grade EXPLORE (2010)</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>ADEQUATE_YEARLY_PROGRESS_MADE_</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>AVERAGE_STUDENT_ATTENDANCE</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
        <tr>
            <td>AVERAGE_TEACHER_ATTENDANCE</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
        <tr>
            <td>CITY</td>
            <td>VARCHAR</td>
            <td>7</td>
        </tr>
        <tr>
            <td>COLLABORATIVE_NAME</td>
            <td>VARCHAR</td>
            <td>34</td>
        </tr>
        <tr>
            <td>COLLEGE_ELIGIBILITY__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>COLLEGE_ENROLLMENT</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>COLLEGE_ENROLLMENT_RATE__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>COMMUNITY_AREA_NAME</td>
            <td>VARCHAR</td>
            <td>22</td>
        </tr>
        <tr>
            <td>COMMUNITY_AREA_NUMBER</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>CPS_PERFORMANCE_POLICY_LEVEL</td>
            <td>VARCHAR</td>
            <td>15</td>
        </tr>
        <tr>
            <td>CPS_PERFORMANCE_POLICY_STATUS</td>
            <td>VARCHAR</td>
            <td>16</td>
        </tr>
        <tr>
            <td>ENVIRONMENT_ICON</td>
            <td>VARCHAR</td>
            <td>11</td>
        </tr>
        <tr>
            <td>ENVIRONMENT_SCORE</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Elementary, Middle, or High School</td>
            <td>VARCHAR</td>
            <td>2</td>
        </tr>
        <tr>
            <td>FAMILY_INVOLVEMENT_ICON</td>
            <td>VARCHAR</td>
            <td>11</td>
        </tr>
        <tr>
            <td>FAMILY_INVOLVEMENT_SCORE</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>FRESHMAN_ON_TRACK_RATE__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GENERAL_SERVICES_ROUTE</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>GR3_5_GRADE_LEVEL_MATH__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR3_5_GRADE_LEVEL_READ__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR3_5_KEEP_PACE_MATH__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR3_5_KEEP_PACE_READ__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR6_8_GRADE_LEVEL_MATH__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR6_8_GRADE_LEVEL_READ__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR6_8_KEEP_PACE_MATH_</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR6_8_KEEP_PACE_READ__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GRADUATION_RATE__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR_8_EXPLORE_MATH__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>GR_8_EXPLORE_READ__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>HEALTHY_SCHOOL_CERTIFIED</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>INDIVIDUALIZED_EDUCATION_PROGRAM_COMPLIANCE_RATE</td>
            <td>VARCHAR</td>
            <td>7</td>
        </tr>
        <tr>
            <td>INSTRUCTION_ICON</td>
            <td>VARCHAR</td>
            <td>11</td>
        </tr>
        <tr>
            <td>INSTRUCTION_SCORE</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>ISAT_EXCEEDING_MATH__</td>
            <td>DECIMAL</td>
            <td>4</td>
        </tr>
        <tr>
            <td>ISAT_EXCEEDING_READING__</td>
            <td>DECIMAL</td>
            <td>4</td>
        </tr>
        <tr>
            <td>ISAT_VALUE_ADD_COLOR_MATH</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
        <tr>
            <td>ISAT_VALUE_ADD_COLOR_READ</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
        <tr>
            <td>ISAT_VALUE_ADD_MATH</td>
            <td>DECIMAL</td>
            <td>3</td>
        </tr>
        <tr>
            <td>ISAT_VALUE_ADD_READ</td>
            <td>DECIMAL</td>
            <td>3</td>
        </tr>
        <tr>
            <td>LATITUDE</td>
            <td>DECIMAL</td>
            <td>18</td>
        </tr>
        <tr>
            <td>LEADERS_ICON</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>LEADERS_SCORE</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>LINK</td>
            <td>VARCHAR</td>
            <td>78</td>
        </tr>
        <tr>
            <td>LOCATION</td>
            <td>VARCHAR</td>
            <td>27</td>
        </tr>
        <tr>
            <td>LONGITUDE</td>
            <td>DECIMAL</td>
            <td>18</td>
        </tr>
        <tr>
            <td>NAME_OF_SCHOOL</td>
            <td>VARCHAR</td>
            <td>64</td>
        </tr>
        <tr>
            <td>NETWORK_MANAGER</td>
            <td>VARCHAR</td>
            <td>40</td>
        </tr>
        <tr>
            <td>NET_CHANGE_EXPLORE_AND_PLAN</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>NET_CHANGE_PLAN_AND_ACT</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>PARENT_ENGAGEMENT_ICON</td>
            <td>VARCHAR</td>
            <td>7</td>
        </tr>
        <tr>
            <td>PARENT_ENGAGEMENT_SCORE</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>PARENT_ENVIRONMENT_ICON</td>
            <td>VARCHAR</td>
            <td>7</td>
        </tr>
        <tr>
            <td>PARENT_ENVIRONMENT_SCORE</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>PHONE_NUMBER</td>
            <td>VARCHAR</td>
            <td>14</td>
        </tr>
        <tr>
            <td>PK_2_LITERACY__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>PK_2_MATH__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>POLICE_DISTRICT</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>RATE_OF_MISCONDUCTS__PER_100_STUDENTS_</td>
            <td>DECIMAL</td>
            <td>5</td>
        </tr>
        <tr>
            <td>SAFETY_ICON</td>
            <td>VARCHAR</td>
            <td>11</td>
        </tr>
        <tr>
            <td>SAFETY_SCORE</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>SCHOOL_ID</td>
            <td>INTEGER</td>
            <td>4</td>
        </tr>
        <tr>
            <td>STATE</td>
            <td>VARCHAR</td>
            <td>2</td>
        </tr>
        <tr>
            <td>STREET_ADDRESS</td>
            <td>VARCHAR</td>
            <td>29</td>
        </tr>
        <tr>
            <td>STUDENTS_PASSING__ALGEBRA__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>STUDENTS_TAKING__ALGEBRA__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>TEACHERS_ICON</td>
            <td>VARCHAR</td>
            <td>11</td>
        </tr>
        <tr>
            <td>TEACHERS_SCORE</td>
            <td>VARCHAR</td>
            <td>3</td>
        </tr>
        <tr>
            <td>TRACK_SCHEDULE</td>
            <td>VARCHAR</td>
            <td>12</td>
        </tr>
        <tr>
            <td>WARD</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>X_COORDINATE</td>
            <td>DECIMAL</td>
            <td>13</td>
        </tr>
        <tr>
            <td>Y_COORDINATE</td>
            <td>DECIMAL</td>
            <td>13</td>
        </tr>
        <tr>
            <td>ZIP_CODE</td>
            <td>INTEGER</td>
            <td>4</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:

%sql select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

or

%sql select distinct(NAME), COLTYPE, LENGTH from SYSIBM.SYSCOLUMNS where TBNAME = 'SCHOOLS'

-->


### Questions

1.  Is the column name for the "SCHOOL ID" attribute in upper or mixed case?
2.  What is the name of "Community Area Name" column in your table? Does it have spaces?
3.  Are there any columns in whose names the spaces and paranthesis (round brackets) have been replaced by the underscore character "\_"?


## Problems

### Problem 1

##### How many Elementary Schools are in the dataset?



```python
%sql SELECT DISTINCT "Elementary, Middle, or High School" FROM SCHOOLS LIMIT 3;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    (ibm_db_dbi.ProgrammingError) ibm_db_dbi::ProgrammingError: SQLNumResultCols failed: [IBM][CLI Driver][DB2/LINUXX8664] SQL0206N  "Elementary, Middle, or High School" is not valid in the context where it is used.  SQLSTATE=42703 SQLCODE=-206
    [SQL: SELECT DISTINCT "Elementary, Middle, or High School" FROM SCHOOLS LIMIT 3;]
    (Background on this error at: http://sqlalche.me/e/13/f405)



```sql
%%sql
-- RENAMED COLUMN : ALTER TABLE SCHOOLS RENAME COLUMN "Elementary, Middle, or High School" TO SchoolType;
SELECT DISTINCT(SchoolType)
FROM SCHOOLS;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>schooltype</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ES</td>
        </tr>
        <tr>
            <td>HS</td>
        </tr>
        <tr>
            <td>MS</td>
        </tr>
    </tbody>
</table>




```sql
%%sql
-- lets get the count
SELECT COUNT(*) AS ElementaryCount
FROM SCHOOLS
WHERE SchoolType = 'ES';
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>elementarycount</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>462</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
Which column specifies the school type e.g. 'ES', 'MS', 'HS'? ("Elementary School, Middle School, High School")
-->


Double-click **here** for another hint

<!--
Does the column name have mixed case, spaces or other special characters?
If so, ensure you use double quotes around the "Name of the Column"
-->


Double-click **here** for the solution.

<!-- Solution:

%sql select count(*) from SCHOOLS where "Elementary, Middle, or High School" = 'ES'

Correct answer: 462

-->


### Problem 2

##### What is the highest Safety Score?



```python
%sql SELECT MAX(SAFETY_SCORE) AS Max_Safety_Score FROM SCHOOLS;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>max_safety_score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>99</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
Use the MAX() function
-->


Double-click **here** for the solution.

<!-- Hint:

%sql select MAX(Safety_Score) AS MAX_SAFETY_SCORE from SCHOOLS

Correct answer: 99
-->


### Problem 3

##### Which schools have highest Safety Score?



```sql
%%sql
-- using subquery
SELECT NAME_OF_SCHOOL, SAFETY_SCORE
FROM SCHOOLS
WHERE SAFETY_SCORE = (SELECT MAX(SAFETY_SCORE) FROM SCHOOLS)
ORDER BY NAME_OF_SCHOOL ASC;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>safety_score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Abraham Lincoln Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Alexander Graham Bell Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Annie Keller Elementary Gifted Magnet School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Augustus H Burley Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Edgar Allan Poe Elementary Classical School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Edgebrook Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Ellen Mitchell Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>James E McDade Elementary Classical School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>James G Blaine Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>LaSalle Elementary Language Academy</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Mary E Courtenay Elementary Language Arts Center</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Northside College Preparatory High School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Northside Learning Center High School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Norwood Park Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Oriole Park Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Sauganash Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Stephen Decatur Classical Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Talman Elementary School</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Wildwood Elementary School</td>
            <td>99</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:
In the previous problem we found out that the highest Safety Score is 99, so we can use that as an input in the where clause:

%sql select Name_of_School, Safety_Score from SCHOOLS where Safety_Score = 99

or, a better way:

%sql select Name_of_School, Safety_Score from SCHOOLS where \
  Safety_Score= (select MAX(Safety_Score) from SCHOOLS)


Correct answer: several schools with with Safety Score of 99.
-->


### Problem 4

##### What are the top 10 schools with the highest "Average Student Attendance"?



```python
# Which Column Would This Be USE LOWER for casing and like search to get likely culprits to find attendance details
%sql SELECT colname, typename, length \
     FROM SYSCAT.COLUMNS \
     WHERE tabname = 'SCHOOLS' and tabschema = 'CGV02624' AND LOWER(colname) LIKE '%attendance%';
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>colname</th>
            <th>typename</th>
            <th>length</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AVERAGE_STUDENT_ATTENDANCE</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
        <tr>
            <td>AVERAGE_TEACHER_ATTENDANCE</td>
            <td>VARCHAR</td>
            <td>6</td>
        </tr>
    </tbody>
</table>




```python
# Don't forget Nulls/None exclusion
%sql SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE \
     FROM SCHOOLS \
     ORDER BY AVERAGE_STUDENT_ATTENDANCE DESC NULLS LAST \
     LIMIT 10;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>average_student_attendance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Charles Haines Elementary School</td>
            <td>98.40%</td>
        </tr>
        <tr>
            <td>James Ward Elementary School</td>
            <td>97.80%</td>
        </tr>
        <tr>
            <td>Edgar Allan Poe Elementary Classical School</td>
            <td>97.60%</td>
        </tr>
        <tr>
            <td>Orozco Fine Arts &amp; Sciences Elementary School</td>
            <td>97.60%</td>
        </tr>
        <tr>
            <td>Rachel Carson Elementary School</td>
            <td>97.60%</td>
        </tr>
        <tr>
            <td>Annie Keller Elementary Gifted Magnet School</td>
            <td>97.50%</td>
        </tr>
        <tr>
            <td>Andrew Jackson Elementary Language Academy</td>
            <td>97.40%</td>
        </tr>
        <tr>
            <td>Lenart Elementary Regional Gifted Center</td>
            <td>97.40%</td>
        </tr>
        <tr>
            <td>Disney II Magnet School</td>
            <td>97.30%</td>
        </tr>
        <tr>
            <td>John H Vanderpoel Elementary Magnet School</td>
            <td>97.20%</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:

%sql select Name_of_School, Average_Student_Attendance from SCHOOLS \
    order by Average_Student_Attendance desc nulls last limit 10 

-->


### Problem 5

##### Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance



```python
%sql SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE \
     FROM SCHOOLS \
     ORDER BY AVERAGE_STUDENT_ATTENDANCE ASC NULLS LAST \
     LIMIT 5;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>average_student_attendance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Richard T Crane Technical Preparatory High School</td>
            <td>57.90%</td>
        </tr>
        <tr>
            <td>Barbara Vick Early Childhood &amp; Family Center</td>
            <td>60.90%</td>
        </tr>
        <tr>
            <td>Dyett High School</td>
            <td>62.50%</td>
        </tr>
        <tr>
            <td>Wendell Phillips Academy High School</td>
            <td>63.00%</td>
        </tr>
        <tr>
            <td>Orr Academy High School</td>
            <td>66.30%</td>
        </tr>
    </tbody>
</table>




```python
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     order by Average_Student_Attendance NULLS LAST\
     fetch first 5 rows only
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>average_student_attendance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Richard T Crane Technical Preparatory High School</td>
            <td>57.90%</td>
        </tr>
        <tr>
            <td>Barbara Vick Early Childhood &amp; Family Center</td>
            <td>60.90%</td>
        </tr>
        <tr>
            <td>Dyett High School</td>
            <td>62.50%</td>
        </tr>
        <tr>
            <td>Wendell Phillips Academy High School</td>
            <td>63.00%</td>
        </tr>
        <tr>
            <td>Orr Academy High School</td>
            <td>66.30%</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:

%sql SELECT Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     order by Average_Student_Attendance \
     fetch first 5 rows only

-->


### Problem 6

##### Now remove the '%' sign from the above result set for Average Student Attendance column



```python
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') AS AverageStudentAttendancePerc \
     from SCHOOLS \
     order by Average_Student_Attendance NULLS LAST\
     fetch first 5 rows only
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>averagestudentattendanceperc</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Richard T Crane Technical Preparatory High School</td>
            <td>57.90</td>
        </tr>
        <tr>
            <td>Barbara Vick Early Childhood &amp; Family Center</td>
            <td>60.90</td>
        </tr>
        <tr>
            <td>Dyett High School</td>
            <td>62.50</td>
        </tr>
        <tr>
            <td>Wendell Phillips Academy High School</td>
            <td>63.00</td>
        </tr>
        <tr>
            <td>Orr Academy High School</td>
            <td>66.30</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
Use the REPLACE() function to replace '%' with ''
See documentation for this function at:
https://www.ibm.com/support/knowledgecenter/en/SSEPGG_10.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0000843.html
-->


Double-click **here** for the solution.

<!-- Hint:

%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from SCHOOLS \
     order by Average_Student_Attendance \
     fetch first 5 rows only

-->


### Problem 7

##### Which Schools have Average Student Attendance lower than 70%?



```python
%sql SELECT Name_of_School, Average_Student_Attendance \
     FROM SCHOOLS \
     WHERE CAST(REPLACE(Average_Student_Attendance, '%', '') AS DECFLOAT ) < 70 \
     LIMIT 10;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>average_student_attendance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Barbara Vick Early Childhood &amp; Family Center</td>
            <td>60.90%</td>
        </tr>
        <tr>
            <td>Chicago Vocational Career Academy High School</td>
            <td>68.80%</td>
        </tr>
        <tr>
            <td>Dyett High School</td>
            <td>62.50%</td>
        </tr>
        <tr>
            <td>Manley Career Academy High School</td>
            <td>66.80%</td>
        </tr>
        <tr>
            <td>Orr Academy High School</td>
            <td>66.30%</td>
        </tr>
        <tr>
            <td>Richard T Crane Technical Preparatory High School</td>
            <td>57.90%</td>
        </tr>
        <tr>
            <td>Roberto Clemente Community Academy High School</td>
            <td>69.60%</td>
        </tr>
        <tr>
            <td>Wendell Phillips Academy High School</td>
            <td>63.00%</td>
        </tr>
    </tbody>
</table>




```python
# Double checking some logic with the casting return
%sql SELECT Name_of_School, Average_Student_Attendance \
     FROM SCHOOLS \
     WHERE CAST(REPLACE(Average_Student_Attendance, '%', '') AS DECFLOAT ) < 71 \
     ORDER BY Average_Student_Attendance DESC \
     LIMIT 10;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>average_student_attendance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hyde Park Academy High School</td>
            <td>70.50%</td>
        </tr>
        <tr>
            <td>Austin Polytechnical Academy High School</td>
            <td>70.10%</td>
        </tr>
        <tr>
            <td>Roberto Clemente Community Academy High School</td>
            <td>69.60%</td>
        </tr>
        <tr>
            <td>Chicago Vocational Career Academy High School</td>
            <td>68.80%</td>
        </tr>
        <tr>
            <td>Manley Career Academy High School</td>
            <td>66.80%</td>
        </tr>
        <tr>
            <td>Orr Academy High School</td>
            <td>66.30%</td>
        </tr>
        <tr>
            <td>Wendell Phillips Academy High School</td>
            <td>63.00%</td>
        </tr>
        <tr>
            <td>Dyett High School</td>
            <td>62.50%</td>
        </tr>
        <tr>
            <td>Barbara Vick Early Childhood &amp; Family Center</td>
            <td>60.90%</td>
        </tr>
        <tr>
            <td>Richard T Crane Technical Preparatory High School</td>
            <td>57.90%</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
The datatype of the "Average_Student_Attendance" column is varchar.
So you cannot use it as is in the where clause for a numeric comparison.
First use the CAST() function to cast it as a DECIMAL or DOUBLE
e.g. CAST("Column_Name" as DOUBLE)
or simply: DECIMAL("Column_Name")
-->


Double-click **here** for another hint

<!--
Don't forget the '%' age sign needs to be removed before casting
-->


Double-click **here** for the solution.

<!-- Solution:

%sql SELECT Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance
     
or,

%sql SELECT Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     where DECIMAL ( REPLACE(Average_Student_Attendance, '%', '') ) < 70 \
     order by Average_Student_Attendance

-->


### Problem 8

##### Get the total College Enrollment for each Community Area



```python
# Find the right columns
%sql SELECT colname, typename, length \
     FROM SYSCAT.COLUMNS \
     WHERE tabname = 'SCHOOLS' and tabschema = 'CGV02624' AND (LOWER(colname) LIKE '%enrollment%' OR LOWER(colname) LIKE '%community%' OR LOWER(colname) LIKE '%hardship%');
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>colname</th>
            <th>typename</th>
            <th>length</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>COLLEGE_ENROLLMENT</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
        <tr>
            <td>COLLEGE_ENROLLMENT_RATE__</td>
            <td>VARCHAR</td>
            <td>4</td>
        </tr>
        <tr>
            <td>COMMUNITY_AREA_NAME</td>
            <td>VARCHAR</td>
            <td>22</td>
        </tr>
        <tr>
            <td>COMMUNITY_AREA_NUMBER</td>
            <td>SMALLINT</td>
            <td>2</td>
        </tr>
    </tbody>
</table>




```python
# COLLEGE_ENROLLMENT & COMMUNITY_AREA_NAME
%sql SELECT community_area_name, SUM(college_enrollment) AS total_community_enrollment \
     FROM SCHOOLS \
     GROUP BY community_area_name \
     ORDER BY total_community_enrollment DESC \
     LIMIT 15;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>community_area_name</th>
            <th>total_community_enrollment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>SOUTH LAWNDALE</td>
            <td>14793</td>
        </tr>
        <tr>
            <td>BELMONT CRAGIN</td>
            <td>14386</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>10933</td>
        </tr>
        <tr>
            <td>GAGE PARK</td>
            <td>9915</td>
        </tr>
        <tr>
            <td>BRIGHTON PARK</td>
            <td>9647</td>
        </tr>
        <tr>
            <td>WEST TOWN</td>
            <td>9429</td>
        </tr>
        <tr>
            <td>HUMBOLDT PARK</td>
            <td>8620</td>
        </tr>
        <tr>
            <td>WEST RIDGE</td>
            <td>8197</td>
        </tr>
        <tr>
            <td>NEAR WEST SIDE</td>
            <td>7975</td>
        </tr>
        <tr>
            <td>NEW CITY</td>
            <td>7922</td>
        </tr>
        <tr>
            <td>IRVING PARK</td>
            <td>7764</td>
        </tr>
        <tr>
            <td>NORTH CENTER</td>
            <td>7541</td>
        </tr>
        <tr>
            <td>LOGAN SQUARE</td>
            <td>7351</td>
        </tr>
        <tr>
            <td>LOWER WEST SIDE</td>
            <td>7257</td>
        </tr>
        <tr>
            <td>CHICAGO LAWN</td>
            <td>7086</td>
        </tr>
    </tbody>
</table>




```python
# Calculate Running Total for Austin to Check for Above
%sql SELECT community_area_name, college_enrollment, SUM(college_enrollment) OVER(ORDER BY college_enrollment ASC) AS RunningTotal \
     FROM SCHOOLS \
     WHERE LOWER(community_area_name) LIKE '%austin%';
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>community_area_name</th>
            <th>college_enrollment</th>
            <th>runningtotal</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AUSTIN</td>
            <td>93</td>
            <td>93</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>182</td>
            <td>275</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>250</td>
            <td>525</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>297</td>
            <td>822</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>301</td>
            <td>1123</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>316</td>
            <td>1439</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>354</td>
            <td>1793</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>377</td>
            <td>2170</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>393</td>
            <td>2563</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>410</td>
            <td>2973</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>422</td>
            <td>3395</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>458</td>
            <td>3853</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>460</td>
            <td>4313</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>490</td>
            <td>4803</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>524</td>
            <td>5327</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>554</td>
            <td>5881</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>565</td>
            <td>6446</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>576</td>
            <td>7022</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>605</td>
            <td>7627</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>658</td>
            <td>8285</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>726</td>
            <td>9011</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>811</td>
            <td>9822</td>
        </tr>
        <tr>
            <td>AUSTIN</td>
            <td>1111</td>
            <td>10933</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
Verify the exact name of the Enrollment column in the database
Use the SUM() function to add up the Enrollments for each Community Area
-->


Double-click **here** for another hint

<!--
Don't forget to group by the Community Area
-->


Double-click **here** for the solution.

<!-- Solution:

%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by Community_Area_Name 

-->


### Problem 9

##### Get the 5 Community Areas with the least total College Enrollment  sorted in ascending order



```sql
%%sql
SELECT Community_Area_Name, SUM(college_enrollment) AS total_enrollment
FROM SCHOOLS
GROUP BY Community_Area_Name
ORDER BY total_enrollment ASC
LIMIT 5;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>community_area_name</th>
            <th>total_enrollment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>OAKLAND</td>
            <td>140</td>
        </tr>
        <tr>
            <td>FULLER PARK</td>
            <td>531</td>
        </tr>
        <tr>
            <td>BURNSIDE</td>
            <td>549</td>
        </tr>
        <tr>
            <td>OHARE</td>
            <td>786</td>
        </tr>
        <tr>
            <td>LOOP</td>
            <td>871</td>
        </tr>
    </tbody>
</table>



Double-click **here** for a hint

<!--
Order the previous query and limit the number of rows you fetch
-->


Double-click **here** for the solution.

<!-- Solution:

%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   fetch first 5 rows only

-->


### Problem 10

##### List 5 schools with lowest safety score.



```sql
%%sql
SELECT name_of_school, safety_score
FROM SCHOOLS
ORDER BY safety_score ASC
LIMIT 5;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>name_of_school</th>
            <th>safety_score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Edmond Burke Elementary School</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Luke O&#x27;Toole Elementary School</td>
            <td>5</td>
        </tr>
        <tr>
            <td>George W Tilton Elementary School</td>
            <td>6</td>
        </tr>
        <tr>
            <td>Foster Park Elementary School</td>
            <td>11</td>
        </tr>
        <tr>
            <td>Emil G Hirsch Metropolitan High School</td>
            <td>13</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:

%sql SELECT name_of_school, safety_score \
FROM schools \
ORDER BY safety_score \
LIMIT 5
-->


### Problem 11

##### Get the hardship index for the community area which has College Enrollment of 4368



```sql
%%sql 
select hardship_index 
   from chicago_socioeconomic_data CD, schools CPS 
   where CD.ca = CPS.community_area_number 
      and college_enrollment = 4368
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>hardship_index</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>6.0</td>
        </tr>
    </tbody>
</table>




```sql
%%sql
-- No Grouped by Area Has the total
SELECT community_area_name, SUM(college_enrollment) AS total_community_college_enrollment
    FROM SCHOOLS
    GROUP BY community_area_name
    HAVING SUM(college_enrollment) BETWEEN 4250 AND 4500;
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>community_area_name</th>
            <th>total_community_college_enrollment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>KENWOOD</td>
            <td>4287</td>
        </tr>
        <tr>
            <td>UPTOWN</td>
            <td>4388</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:
NOTE: For this solution to work the CHICAGO_SOCIOECONOMIC_DATA table 
      as created in the last lab of Week 3 should already exist

%%sql 
select hardship_index 
   from chicago_socioeconomic_data CD, schools CPS 
   where CD.ca = CPS.community_area_number 
      and college_enrollment = 4368

-->


### Problem 12

##### Get the hardship index for the community area which has the school with the  highest enrollment.



```sql
%%sql 
SELECT CD.ca, CD.hardship_index, CPS.community_area_name, CPS.college_enrollment 
   FROM chicago_socioeconomic_data CD, schools CPS 
   WHERE CD.ca = CPS.community_area_number 
      AND CPS.college_enrollment = (SELECT MAX(college_enrollment) FROM SCHOOLS);
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>ca</th>
            <th>hardship_index</th>
            <th>community_area_name</th>
            <th>college_enrollment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5.0</td>
            <td>6.0</td>
            <td>NORTH CENTER</td>
            <td>4368</td>
        </tr>
    </tbody>
</table>



Double-click **here** for the solution.

<!-- Solution:
NOTE: For this solution to work the CHICAGO_SOCIOECONOMIC_DATA table 
      as created in the last lab of Week 3 should already exist

%sql select ca, community_area_name, hardship_index from chicago_socioeconomic_data \
   where ca in \
   ( select community_area_number from schools order by college_enrollment desc limit 1 )

-->



```python
%sql select ca, community_area_name, hardship_index from chicago_socioeconomic_data \
   where ca in \
   ( select community_area_number from schools order by college_enrollment desc limit 1 )
```

     * ibm_db_sa://cgv02624:***@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb
    Done.





<table>
    <thead>
        <tr>
            <th>ca</th>
            <th>community_area_name</th>
            <th>hardship_index</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5.0</td>
            <td>North Center</td>
            <td>6.0</td>
        </tr>
    </tbody>
</table>



## Summary

##### In this lab you learned how to work with a real word dataset using SQL and Python. You learned how to query columns with spaces or special characters in their names and with mixed case names. You also used built in database functions and practiced how to sort, limit, and order result sets, as well as used sub-queries and worked with multiple tables.


## Author

<a href="https://www.linkedin.com/in/ravahuja/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01" target="_blank">Rav Ahuja</a>

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                        |
| ----------------- | ------- | ----------------- | ----------------------------------------- |
| 2021-07-09        | 2.4     | Malika            | Updated connection string                 |
| 2021-05-19        | 2.3     | Lakshmi Holla     | Updated question                          |
| 2021-04-20        | 2.2     | Malika            | Added the libraries                       |
| 2020-11-27        | 2.1     | Sannareddy Ramesh | Modified data sets and added new problems |
| 2020-08-28        | 2.0     | Lavanya           | Moved lab to course repo in GitLab        |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

