
# Python Libraries

Python, like other programming languages, has an abundance of additional modules or libraries that augument the base framework and functionality of the language.

Think of a library as a collection of functions that can be accessed to complete certain programming tasks without having to write your own algorithm.

For this course, we will focus primarily on the following libraries:

* **Numpy** is a library for working with arrays of data.

* **Pandas** provides high-performance, easy-to-use data structures and data analysis tools.

* **Scipy** is a library of techniques for numerical and scientific computing.

* **Matplotlib** is a library for making graphs.

* **Seaborn** is a higher-level interface to Matplotlib that can be used to simplify many graphing tasks.

* **Statsmodels** is a library that implements many statistical techniques.

# Documentation

Reliable and accesible documentation is an absolute necessity when it comes to knowledge transfer of programming languages.  Luckily, python provides a significant amount of detailed documentation that explains the ins and outs of the language syntax, libraries, and more.  

Understanding how to read documentation is crucial for any programmer as it will serve as a fantastic resource when learning the intricacies of python.

Here is the link to the documentation of the python standard library: [Python Standard Library](https://docs.python.org/3/library/index.html#library-index)

### Importing Libraries

When using Python, you must always begin your scripts by importing the libraries that you will be using. 

The following statement imports the numpy and pandas library, and gives them abbreviated names:


```python
import numpy as np
import pandas as pd
```

### Utilizing Library Functions

After importing a library, its functions can then be called from your code by prepending the library name to the function name.  For example, to use the '`dot`' function from the '`numpy`' library, you would enter '`numpy.dot`'.  To avoid repeatedly having to type the libary name in your scripts, it is conventional to define a two or three letter abbreviation for each library, e.g. '`numpy`' is usually abbreviated as '`np`'.  This allows us to use '`np.dot`' instead of '`numpy.dot`'.  Similarly, the Pandas library is typically abbreviated as '`pd`'.

The next cell shows how to call functions within an imported library:


```python
a = np.array([0,1,2,3,4,5,6,7,8,9,10]) 
np.mean(a)
```




    5.0



As you can see, we used the mean() function within the numpy library to calculate the mean of the numpy 1-dimensional array.

# Data Management

Data management is a crucial component to statistical analysis and data science work.  The following code will show how to import data via the pandas library, view your data, and transform your data.

The main data structure that Pandas works with is called a **Data Frame**.  This is a two-dimensional table of data in which the rows typically represent cases (e.g. Cartwheel Contest Participants), and the columns represent variables.  Pandas also has a one-dimensional data structure called a **Series** that we will encounter when accesing a single column of a Data Frame.

Pandas has a variety of functions named '`read_xxx`' for reading data in different formats.  Right now we will focus on reading '`csv`' files, which stands for comma-separated values. However the other file formats include excel, json, and sql just to name a few.

This is a link to the .csv that we will be exploring in this tutorial: [Cartwheel Data](https://www.coursera.org/learn/understanding-visualization-data/resources/0rVxx) (Link goes to the dataset section of the Resources for this course)

There are many other options to '`read_csv`' that are very useful.  For example, you would use the option `sep='\t'` instead of the default `sep=','` if the fields of your data file are delimited by tabs instead of commas.  See [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) for the full documentation for '`read_csv`'.

### Importing Data


```python
# Store the url string that hosts our .csv file (note that this is a different url than in the video)
url = "Cartwheeldata.csv"

# Read the .csv file and store it as a pandas Data Frame
df = pd.read_csv(url)

# Output object type
type(df)
```




    pandas.core.frame.DataFrame



### Viewing Data


```python
# We can view our Data Frame by calling the head() function
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>GenderGroup</th>
      <th>Glasses</th>
      <th>GlassesGroup</th>
      <th>Height</th>
      <th>Wingspan</th>
      <th>CWDistance</th>
      <th>Complete</th>
      <th>CompleteGroup</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>56</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.0</td>
      <td>61.0</td>
      <td>79</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>26</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.0</td>
      <td>60.0</td>
      <td>70</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>33</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>66.0</td>
      <td>64.0</td>
      <td>85</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>39</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>64.0</td>
      <td>63.0</td>
      <td>87</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>27</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>73.0</td>
      <td>75.0</td>
      <td>72</td>
      <td>N</td>
      <td>0</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



The head() function simply shows the first 5 rows of our Data Frame.  If we wanted to show the entire Data Frame we would simply write the following:


```python
# Output entire Data Frame
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>GenderGroup</th>
      <th>Glasses</th>
      <th>GlassesGroup</th>
      <th>Height</th>
      <th>Wingspan</th>
      <th>CWDistance</th>
      <th>Complete</th>
      <th>CompleteGroup</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>56</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.00</td>
      <td>61.0</td>
      <td>79</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>26</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.00</td>
      <td>60.0</td>
      <td>70</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>33</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>66.00</td>
      <td>64.0</td>
      <td>85</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>39</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>64.00</td>
      <td>63.0</td>
      <td>87</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>27</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>73.00</td>
      <td>75.0</td>
      <td>72</td>
      <td>N</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>24</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>75.00</td>
      <td>71.0</td>
      <td>81</td>
      <td>N</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>28</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>75.00</td>
      <td>76.0</td>
      <td>107</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>22</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>65.00</td>
      <td>62.0</td>
      <td>98</td>
      <td>Y</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>29</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>74.00</td>
      <td>73.0</td>
      <td>106</td>
      <td>N</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>33</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>63.00</td>
      <td>60.0</td>
      <td>65</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>30</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>69.50</td>
      <td>66.0</td>
      <td>96</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>28</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.75</td>
      <td>58.0</td>
      <td>79</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>25</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>65.00</td>
      <td>64.5</td>
      <td>92</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>23</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>61.50</td>
      <td>57.5</td>
      <td>66</td>
      <td>Y</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>31</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>73.00</td>
      <td>74.0</td>
      <td>72</td>
      <td>Y</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>26</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>71.00</td>
      <td>72.0</td>
      <td>115</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>26</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>61.50</td>
      <td>59.5</td>
      <td>90</td>
      <td>N</td>
      <td>0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>27</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>66.00</td>
      <td>66.0</td>
      <td>74</td>
      <td>Y</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>23</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>70.00</td>
      <td>69.0</td>
      <td>64</td>
      <td>Y</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>24</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>68.00</td>
      <td>66.0</td>
      <td>85</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>23</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>69.00</td>
      <td>67.0</td>
      <td>66</td>
      <td>N</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>29</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>71.00</td>
      <td>70.0</td>
      <td>101</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>25</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>70.00</td>
      <td>68.0</td>
      <td>82</td>
      <td>Y</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>26</td>
      <td>M</td>
      <td>2</td>
      <td>N</td>
      <td>0</td>
      <td>69.00</td>
      <td>71.0</td>
      <td>63</td>
      <td>Y</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>23</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>65.00</td>
      <td>63.0</td>
      <td>67</td>
      <td>N</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



As you can see, we have a 2-Dimensional object where each row is an independent observation of our cartwheel data.

To gather more information regarding the data, we can view the column names and data types of each column with the following functions:


```python
df.columns
```




    Index([u'ID', u'Age', u'Gender', u'GenderGroup', u'Glasses', u'GlassesGroup',
           u'Height', u'Wingspan', u'CWDistance', u'Complete', u'CompleteGroup',
           u'Score'],
          dtype='object')



Lets say we would like to splice our data frame and select only specific portions of our data.  There are three different ways of doing so.

1. .loc()
2. .iloc()
3. .ix()

We will cover the .loc() and .iloc() splicing functions.

### .loc()
.loc() takes two single/list/range operator separated by ','. The first one indicates the row and the second one indicates columns.


```python
# Return all observations of CWDistance
df.loc[:,"CWDistance"]
```




    0      79
    1      70
    2      85
    3      87
    4      72
    5      81
    6     107
    7      98
    8     106
    9      65
    10     96
    11     79
    12     92
    13     66
    14     72
    15    115
    16     90
    17     74
    18     64
    19     85
    20     66
    21    101
    22     82
    23     63
    24     67
    Name: CWDistance, dtype: int64




```python
# Select all rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
df.loc[:,["CWDistance", "Height", "Wingspan"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CWDistance</th>
      <th>Height</th>
      <th>Wingspan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79</td>
      <td>62.00</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>70</td>
      <td>62.00</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>85</td>
      <td>66.00</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>87</td>
      <td>64.00</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72</td>
      <td>73.00</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>81</td>
      <td>75.00</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>107</td>
      <td>75.00</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>98</td>
      <td>65.00</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>106</td>
      <td>74.00</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>65</td>
      <td>63.00</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>96</td>
      <td>69.50</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>79</td>
      <td>62.75</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>92</td>
      <td>65.00</td>
      <td>64.5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>66</td>
      <td>61.50</td>
      <td>57.5</td>
    </tr>
    <tr>
      <th>14</th>
      <td>72</td>
      <td>73.00</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>115</td>
      <td>71.00</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>90</td>
      <td>61.50</td>
      <td>59.5</td>
    </tr>
    <tr>
      <th>17</th>
      <td>74</td>
      <td>66.00</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>64</td>
      <td>70.00</td>
      <td>69.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>85</td>
      <td>68.00</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>66</td>
      <td>69.00</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>101</td>
      <td>71.00</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>82</td>
      <td>70.00</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>63</td>
      <td>69.00</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>67</td>
      <td>65.00</td>
      <td>63.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select few rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
df.loc[:9, ["CWDistance", "Height", "Wingspan"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CWDistance</th>
      <th>Height</th>
      <th>Wingspan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79</td>
      <td>62.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>70</td>
      <td>62.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>85</td>
      <td>66.0</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>87</td>
      <td>64.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72</td>
      <td>73.0</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>81</td>
      <td>75.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>107</td>
      <td>75.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>98</td>
      <td>65.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>106</td>
      <td>74.0</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>65</td>
      <td>63.0</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select range of rows for all columns
df.loc[10:15]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>GenderGroup</th>
      <th>Glasses</th>
      <th>GlassesGroup</th>
      <th>Height</th>
      <th>Wingspan</th>
      <th>CWDistance</th>
      <th>Complete</th>
      <th>CompleteGroup</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>30</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>69.50</td>
      <td>66.0</td>
      <td>96</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>28</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.75</td>
      <td>58.0</td>
      <td>79</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>25</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>65.00</td>
      <td>64.5</td>
      <td>92</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>23</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>61.50</td>
      <td>57.5</td>
      <td>66</td>
      <td>Y</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>31</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>73.00</td>
      <td>74.0</td>
      <td>72</td>
      <td>Y</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>26</td>
      <td>M</td>
      <td>2</td>
      <td>Y</td>
      <td>1</td>
      <td>71.00</td>
      <td>72.0</td>
      <td>115</td>
      <td>Y</td>
      <td>1</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



The .loc() function requires to arguments, the indices of the rows and the column names you wish to observe.

In the above case **:** specifies all rows, and our column is **CWDistance**. df.loc[**:**,**"CWDistance"**]

Now, let's say we only want to return the first 10 observations:


```python
df.loc[:9, "CWDistance"]
```




    0     79
    1     70
    2     85
    3     87
    4     72
    5     81
    6    107
    7     98
    8    106
    9     65
    Name: CWDistance, dtype: int64



### .iloc()
.iloc() is integer based slicing, whereas .loc() used labels/column names. Here are some examples:


```python
df.iloc[:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Age</th>
      <th>Gender</th>
      <th>GenderGroup</th>
      <th>Glasses</th>
      <th>GlassesGroup</th>
      <th>Height</th>
      <th>Wingspan</th>
      <th>CWDistance</th>
      <th>Complete</th>
      <th>CompleteGroup</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>56</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.0</td>
      <td>61.0</td>
      <td>79</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>26</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>62.0</td>
      <td>60.0</td>
      <td>70</td>
      <td>Y</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>33</td>
      <td>F</td>
      <td>1</td>
      <td>Y</td>
      <td>1</td>
      <td>66.0</td>
      <td>64.0</td>
      <td>85</td>
      <td>Y</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>39</td>
      <td>F</td>
      <td>1</td>
      <td>N</td>
      <td>0</td>
      <td>64.0</td>
      <td>63.0</td>
      <td>87</td>
      <td>Y</td>
      <td>1</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:5, 2:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>GenderGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:5, ["Gender", "GenderGroup"]]
```


    

    TypeErrorTraceback (most recent call last)

    <ipython-input-14-38420b6cd49e> in <module>()
    ----> 1 df.iloc[1:5, ["Gender", "GenderGroup"]]
    

    /opt/conda/envs/python2/lib/python2.7/site-packages/pandas/core/indexing.pyc in __getitem__(self, key)
       1470             except (KeyError, IndexError):
       1471                 pass
    -> 1472             return self._getitem_tuple(key)
       1473         else:
       1474             # we by definition only have the 0th axis


    /opt/conda/envs/python2/lib/python2.7/site-packages/pandas/core/indexing.pyc in _getitem_tuple(self, tup)
       2011     def _getitem_tuple(self, tup):
       2012 
    -> 2013         self._has_valid_tuple(tup)
       2014         try:
       2015             return self._getitem_lowerdim(tup)


    /opt/conda/envs/python2/lib/python2.7/site-packages/pandas/core/indexing.pyc in _has_valid_tuple(self, key)
        220                 raise IndexingError('Too many indexers')
        221             try:
    --> 222                 self._validate_key(k, i)
        223             except ValueError:
        224                 raise ValueError("Location based indexing can only have "


    /opt/conda/envs/python2/lib/python2.7/site-packages/pandas/core/indexing.pyc in _validate_key(self, key, axis)
       1965             l = len(self.obj._get_axis(axis))
       1966 
    -> 1967             if len(arr) and (arr.max() >= l or arr.min() < -l):
       1968                 raise IndexError("positional indexers are out-of-bounds")
       1969         else:


    /opt/conda/envs/python2/lib/python2.7/site-packages/numpy/core/_methods.pyc in _amax(a, axis, out, keepdims, initial)
         26 def _amax(a, axis=None, out=None, keepdims=False,
         27           initial=_NoValue):
    ---> 28     return umr_maximum(a, axis, None, out, keepdims, initial)
         29 
         30 def _amin(a, axis=None, out=None, keepdims=False,


    TypeError: cannot perform reduce with flexible type


We can view the data types of our data frame columns with by calling .dtypes on our data frame:


```python
df.dtypes
```




    ID                 int64
    Age                int64
    Gender            object
    GenderGroup        int64
    Glasses           object
    GlassesGroup       int64
    Height           float64
    Wingspan         float64
    CWDistance         int64
    Complete          object
    CompleteGroup      int64
    Score              int64
    dtype: object



The output indicates we have integers, floats, and objects with our Data Frame.

We may also want to observe the different unique values within a specific column, lets do this for Gender:


```python
# List unique values in the df['Gender'] column
df.Gender.unique()
```




    array(['F', 'M'], dtype=object)




```python
# Lets explore df["GenderGroup] as well
df.GenderGroup.unique()
```




    array([1, 2])



It seems that these fields may serve the same purpose, which is to specify male vs. female. Lets check this quickly by observing only these two columns:


```python
# Use .loc() to specify a list of mulitple column names
df.loc[:,["Gender", "GenderGroup"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>GenderGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>18</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>F</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>22</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>23</th>
      <td>M</td>
      <td>2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>F</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



From eyeballing the output, it seems to check out.  We can streamline this by utilizing the groupby() and size() functions.


```python
df.groupby(['Gender','GenderGroup']).size()
```




    Gender  GenderGroup
    F       1              12
    M       2              13
    dtype: int64



This output indicates that we have two types of combinations. 

* Case 1: Gender = F & Gender Group = 1 
* Case 2: Gender = M & GenderGroup = 2.  

This validates our initial assumption that these two fields essentially portray the same information.
