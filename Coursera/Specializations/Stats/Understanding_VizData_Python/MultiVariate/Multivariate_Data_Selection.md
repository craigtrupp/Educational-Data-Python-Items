
## How to select dataframe subsets from multivariate data


```python
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
```


```python
# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")
```


```python
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
      <th>SEQN</th>
      <th>ALQ101</th>
      <th>ALQ110</th>
      <th>ALQ130</th>
      <th>SMQ020</th>
      <th>RIAGENDR</th>
      <th>RIDAGEYR</th>
      <th>RIDRETH1</th>
      <th>DMDCITZN</th>
      <th>DMDEDUC2</th>
      <th>DMDMARTL</th>
      <th>DMDHHSIZ</th>
      <th>WTINT2YR</th>
      <th>SDMVPSU</th>
      <th>SDMVSTRA</th>
      <th>INDFMPIR</th>
      <th>BPXSY1</th>
      <th>BPXDI1</th>
      <th>BPXSY2</th>
      <th>BPXDI2</th>
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
      <th>HIQ210</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>83732</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>62</td>
      <td>3</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>134671.37</td>
      <td>1</td>
      <td>125</td>
      <td>4.39</td>
      <td>128.0</td>
      <td>70.0</td>
      <td>124.0</td>
      <td>64.0</td>
      <td>94.8</td>
      <td>184.5</td>
      <td>27.8</td>
      <td>43.3</td>
      <td>43.6</td>
      <td>35.9</td>
      <td>101.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>83733</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>1</td>
      <td>1</td>
      <td>53</td>
      <td>3</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>1</td>
      <td>24328.56</td>
      <td>1</td>
      <td>125</td>
      <td>1.32</td>
      <td>146.0</td>
      <td>88.0</td>
      <td>140.0</td>
      <td>88.0</td>
      <td>90.4</td>
      <td>171.4</td>
      <td>30.8</td>
      <td>38.0</td>
      <td>40.0</td>
      <td>33.2</td>
      <td>107.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83734</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>78</td>
      <td>3</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>12400.01</td>
      <td>1</td>
      <td>131</td>
      <td>1.51</td>
      <td>138.0</td>
      <td>46.0</td>
      <td>132.0</td>
      <td>44.0</td>
      <td>83.4</td>
      <td>170.1</td>
      <td>28.8</td>
      <td>35.6</td>
      <td>37.0</td>
      <td>31.0</td>
      <td>116.5</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>83735</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>56</td>
      <td>3</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>1</td>
      <td>102718.00</td>
      <td>1</td>
      <td>131</td>
      <td>5.00</td>
      <td>132.0</td>
      <td>72.0</td>
      <td>134.0</td>
      <td>68.0</td>
      <td>109.8</td>
      <td>160.9</td>
      <td>42.4</td>
      <td>38.5</td>
      <td>37.7</td>
      <td>38.3</td>
      <td>110.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>83736</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>42</td>
      <td>4</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>5</td>
      <td>17627.67</td>
      <td>2</td>
      <td>126</td>
      <td>1.23</td>
      <td>100.0</td>
      <td>70.0</td>
      <td>114.0</td>
      <td>54.0</td>
      <td>55.2</td>
      <td>164.9</td>
      <td>20.3</td>
      <td>37.4</td>
      <td>36.0</td>
      <td>27.2</td>
      <td>80.4</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



### Keep only body measures columns, so only columns with "BMX" in the name


```python
# get columns names
col_names = df.columns
col_names
```




    Index(['SEQN', 'ALQ101', 'ALQ110', 'ALQ130', 'SMQ020', 'RIAGENDR', 'RIDAGEYR',
           'RIDRETH1', 'DMDCITZN', 'DMDEDUC2', 'DMDMARTL', 'DMDHHSIZ', 'WTINT2YR',
           'SDMVPSU', 'SDMVSTRA', 'INDFMPIR', 'BPXSY1', 'BPXDI1', 'BPXSY2',
           'BPXDI2', 'BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
           'BMXWAIST', 'HIQ210'],
          dtype='object')




```python
# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST']
```


```python
# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
[column for column in col_names if 'BMX' in column]
```




    ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC', 'BMXWAIST']




```python
keep = [column for column in col_names if 'BMX' in column]
```


```python
# use [] notation to keep columns
df_BMX = df[keep]
```


```python
df_BMX.head()
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>94.8</td>
      <td>184.5</td>
      <td>27.8</td>
      <td>43.3</td>
      <td>43.6</td>
      <td>35.9</td>
      <td>101.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90.4</td>
      <td>171.4</td>
      <td>30.8</td>
      <td>38.0</td>
      <td>40.0</td>
      <td>33.2</td>
      <td>107.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.4</td>
      <td>170.1</td>
      <td>28.8</td>
      <td>35.6</td>
      <td>37.0</td>
      <td>31.0</td>
      <td>116.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109.8</td>
      <td>160.9</td>
      <td>42.4</td>
      <td>38.5</td>
      <td>37.7</td>
      <td>38.3</td>
      <td>110.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.2</td>
      <td>164.9</td>
      <td>20.3</td>
      <td>37.4</td>
      <td>36.0</td>
      <td>27.2</td>
      <td>80.4</td>
    </tr>
  </tbody>
</table>
</div>



There are two methods for selecting by row and column. 
# link for pandas cheat sheets
* df.loc[row labels or bool, col labels or bool]
* df.iloc[row int or bool, col int or bool]

### [From pandas docs](https://pandas.pydata.org/pandas-docs/stable/indexing.html]):  
* [ ] column indexing
* .loc is primarily label based, but may also be used with a boolean array.   
* .iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.


```python
df.loc[:, keep].head()
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>94.8</td>
      <td>184.5</td>
      <td>27.8</td>
      <td>43.3</td>
      <td>43.6</td>
      <td>35.9</td>
      <td>101.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90.4</td>
      <td>171.4</td>
      <td>30.8</td>
      <td>38.0</td>
      <td>40.0</td>
      <td>33.2</td>
      <td>107.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.4</td>
      <td>170.1</td>
      <td>28.8</td>
      <td>35.6</td>
      <td>37.0</td>
      <td>31.0</td>
      <td>116.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109.8</td>
      <td>160.9</td>
      <td>42.4</td>
      <td>38.5</td>
      <td>37.7</td>
      <td>38.3</td>
      <td>110.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.2</td>
      <td>164.9</td>
      <td>20.3</td>
      <td>37.4</td>
      <td>36.0</td>
      <td>27.2</td>
      <td>80.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
index_bool = np.isin(df.columns, keep)
```


```python
index_bool 
```




    array([False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False,  True,  True,  True,  True,  True,  True,  True,
           False])




```python
df.iloc[:,index_bool].head() # Indexing with boolean list
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>94.8</td>
      <td>184.5</td>
      <td>27.8</td>
      <td>43.3</td>
      <td>43.6</td>
      <td>35.9</td>
      <td>101.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90.4</td>
      <td>171.4</td>
      <td>30.8</td>
      <td>38.0</td>
      <td>40.0</td>
      <td>33.2</td>
      <td>107.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.4</td>
      <td>170.1</td>
      <td>28.8</td>
      <td>35.6</td>
      <td>37.0</td>
      <td>31.0</td>
      <td>116.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109.8</td>
      <td>160.9</td>
      <td>42.4</td>
      <td>38.5</td>
      <td>37.7</td>
      <td>38.3</td>
      <td>110.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.2</td>
      <td>164.9</td>
      <td>20.3</td>
      <td>37.4</td>
      <td>36.0</td>
      <td>27.2</td>
      <td>80.4</td>
    </tr>
  </tbody>
</table>
</div>



### Selection by conditions


```python
# Lets only look at rows who 'BMXWAIST' is larger than the median
waist_median = pd.Series.median(df_BMX['BMXWAIST']) # get the median of 'BMXWAIST'
print(df_BMX['BMXWAIST'].median()) # each column is a series so can get like so as well
```

    98.3



```python
waist_median
```




    98.3




```python
df_BMX[df_BMX['BMXWAIST'] > waist_median].head().sort_values('BMXWAIST', ascending=False) # order top waist_median values
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>83.4</td>
      <td>170.1</td>
      <td>28.8</td>
      <td>35.6</td>
      <td>37.0</td>
      <td>31.0</td>
      <td>116.5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>108.3</td>
      <td>179.4</td>
      <td>33.6</td>
      <td>46.0</td>
      <td>44.1</td>
      <td>38.5</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109.8</td>
      <td>160.9</td>
      <td>42.4</td>
      <td>38.5</td>
      <td>37.7</td>
      <td>38.3</td>
      <td>110.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90.4</td>
      <td>171.4</td>
      <td>30.8</td>
      <td>38.0</td>
      <td>40.0</td>
      <td>33.2</td>
      <td>107.9</td>
    </tr>
    <tr>
      <th>0</th>
      <td>94.8</td>
      <td>184.5</td>
      <td>27.8</td>
      <td>43.3</td>
      <td>43.6</td>
      <td>35.9</td>
      <td>101.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Lets add another condition, that 'BMXLEG' must be less than 32
condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
df_BMX[condition1 & condition2].head() # Using [] method
# Note: can't use 'and' instead of '&'
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>35.4</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>27</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>35.9</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>29.1</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>42.6</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>55</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>35.2</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_BMX.loc[condition1 & condition2, :].head() # Using df.loc[] method
# note that the conditiona are describing the rows to keep
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>35.4</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>27</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>35.9</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>29.1</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>42.6</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>55</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>35.2</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Lets make a small dataframe and give it a new index so can more clearly see the differences between .loc and .iloc
tmp = df_BMX.loc[condition1 & condition2, :].head()
tmp.index = ['a', 'b', 'c', 'd', 'e'] # If you use different years than 2015-2016, this my give an error. Why?
tmp
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>35.4</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>35.9</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>29.1</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>42.6</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>e</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>35.2</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmp.loc[['a', 'b'],'BMXLEG']
```




    a    31.6
    b    31.0
    Name: BMXLEG, dtype: float64




```python
tmp.iloc[[0, 1],3]
```




    a    31.6
    b    31.0
    Name: BMXLEG, dtype: float64



### Common errors and how to read them


```python
tmp[:, 'BMXBMI'] 
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-83067c5cae7c> in <module>()
    ----> 1 tmp[:, 'BMXBMI']
    

    /opt/conda/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       2925             if self.columns.nlevels > 1:
       2926                 return self._getitem_multilevel(key)
    -> 2927             indexer = self.columns.get_loc(key)
       2928             if is_integer(indexer):
       2929                 indexer = [indexer]


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2654                                  'backfill or nearest lookups')
       2655             try:
    -> 2656                 return self._engine.get_loc(key)
       2657             except KeyError:
       2658                 return self._engine.get_loc(self._maybe_cast_indexer(key))


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    TypeError: '(slice(None, None, None), 'BMXBMI')' is an invalid key


### Problem
The above gives: TypeError: unhashable type: 'slice' 

The [ ] method uses hashes to identify the columns to keep, and each column has an associated hash. A 'slice' (a subset of rows and columns) does not have an associated hash, thus causing this TypeError.


```python
tmp.loc[:, 'BMXBMI']
```




    a    35.4
    b    35.9
    c    29.1
    d    42.6
    e    35.2
    Name: BMXBMI, dtype: float64




```python
tmp.loc[:, 'BMXBMI'].values
```




    array([35.4, 35.9, 29.1, 42.6, 35.2])




```python
tmp.iloc[:, 'BMXBMI']
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _has_valid_tuple(self, key)
        222             try:
    --> 223                 self._validate_key(k, i)
        224             except ValueError:


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
       2083             raise ValueError("Can only index by location with "
    -> 2084                              "a [{types}]".format(types=self._valid_types))
       2085 


    ValueError: Can only index by location with a [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array]

    
    During handling of the above exception, another exception occurred:


    ValueError                                Traceback (most recent call last)

    <ipython-input-27-9fa39d4097e1> in <module>()
    ----> 1 tmp.iloc[:, 'BMXBMI']
    

    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in __getitem__(self, key)
       1492             except (KeyError, IndexError, AttributeError):
       1493                 pass
    -> 1494             return self._getitem_tuple(key)
       1495         else:
       1496             # we by definition only have the 0th axis


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _getitem_tuple(self, tup)
       2141     def _getitem_tuple(self, tup):
       2142 
    -> 2143         self._has_valid_tuple(tup)
       2144         try:
       2145             return self._getitem_lowerdim(tup)


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _has_valid_tuple(self, key)
        225                 raise ValueError("Location based indexing can only have "
        226                                  "[{types}] types"
    --> 227                                  .format(types=self._valid_types))
        228 
        229     def _is_nested_tuple_indexer(self, tup):


    ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types


### Problem
The above gives: ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types

'BMXBMI' is not an integer that is less than or equal number of columns -1, or a list of boolean values, so it is the wrong value type. 


```python
tmp.iloc[:, 2]
```




    a    35.4
    b    35.9
    c    29.1
    d    42.6
    e    35.2
    Name: BMXBMI, dtype: float64




```python
tmp.loc[:, 2]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-29-a70ce725ddad> in <module>()
    ----> 1 tmp.loc[:, 2]
    

    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in __getitem__(self, key)
       1492             except (KeyError, IndexError, AttributeError):
       1493                 pass
    -> 1494             return self._getitem_tuple(key)
       1495         else:
       1496             # we by definition only have the 0th axis


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _getitem_tuple(self, tup)
        866     def _getitem_tuple(self, tup):
        867         try:
    --> 868             return self._getitem_lowerdim(tup)
        869         except IndexingError:
        870             pass


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _getitem_lowerdim(self, tup)
        986         for i, key in enumerate(tup):
        987             if is_label_like(key) or isinstance(key, tuple):
    --> 988                 section = self._getitem_axis(key, axis=i)
        989 
        990                 # we have yielded a scalar ?


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
       1910 
       1911         # fall thru to straight lookup
    -> 1912         self._validate_key(key, axis)
       1913         return self._get_label(key, axis=axis)
       1914 


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
       1797 
       1798         if not is_list_like_indexer(key):
    -> 1799             self._convert_scalar_indexer(key, axis)
       1800 
       1801     def _is_scalar_access(self, key):


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
        260         ax = self.obj._get_axis(min(axis, self.ndim - 1))
        261         # a scalar
    --> 262         return ax._convert_scalar_indexer(key, kind=self.name)
        263 
        264     def _convert_slice_indexer(self, key, axis):


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
       2878             elif kind in ['loc'] and is_integer(key):
       2879                 if not self.holds_integer():
    -> 2880                     return self._invalid_indexer('label', key)
       2881 
       2882         return key


    /opt/conda/lib/python3.6/site-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
       3064                         "indexers [{key}] of {kind}".format(
       3065                             form=form, klass=type(self), key=key,
    -> 3066                             kind=type(key)))
       3067 
       3068     # --------------------------------------------------------------------


    TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [2] of <class 'int'>


### Problem
The above code gives: ```TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [2] of <class 'int'>```

2 is not one of the labels (i.e. column names) in the dataframe


```python
# Here is another example of using a boolean list for indexing columns
tmp.loc[:, [False, False, True] +[False]*4]
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
      <th>BMXBMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>35.4</td>
    </tr>
    <tr>
      <th>b</th>
      <td>35.9</td>
    </tr>
    <tr>
      <th>c</th>
      <td>29.1</td>
    </tr>
    <tr>
      <th>d</th>
      <td>42.6</td>
    </tr>
    <tr>
      <th>e</th>
      <td>35.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
tmp.iloc[:, 2]
```




    a    35.4
    b    35.9
    c    29.1
    d    42.6
    e    35.2
    Name: BMXBMI, dtype: float64




```python
# We can use the .loc and .iloc methods to change values within the dataframe
tmp.iloc[0:3,2] = 0 # set rows 0-2 (not inclusive third) and update the value to zero
tmp.iloc[:,2]
```




    a     0.0
    b     0.0
    c     0.0
    d    42.6
    e    35.2
    Name: BMXBMI, dtype: float64




```python
tmp.loc['a':'c','BMXBMI'] = [1]*3
tmp.loc[:,'BMXBMI']
```




    a     1.0
    b     1.0
    c     1.0
    d    42.6
    e    35.2
    Name: BMXBMI, dtype: float64




```python
# We can use the [] method when changing all the values of a column
tmp['BMXBMI'] = range(0, 5)
tmp
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>0</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>1</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>2</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>3</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>e</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>4</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# We will get a warning when using the [] method with conditions to set new values in our dataframe
tmp[tmp.BMXBMI > 2]['BMXBMI'] = [10]*2 # Setting new values to a copy of tmp, but not tmp itself
tmp
# You can see that the above code did not change our dataframe 'tmp'. This
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>0</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>1</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>2</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>3</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>e</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>4</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The correct way to do the above is with .loc or .iloc
tmp.loc[tmp.BMXBMI > 2, 'BMXBMI']  = 10
tmp # Now contains the chances
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
      <th>BMXWT</th>
      <th>BMXHT</th>
      <th>BMXBMI</th>
      <th>BMXLEG</th>
      <th>BMXARML</th>
      <th>BMXARMC</th>
      <th>BMXWAIST</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>80.5</td>
      <td>150.8</td>
      <td>0</td>
      <td>31.6</td>
      <td>32.7</td>
      <td>33.7</td>
      <td>113.5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>75.6</td>
      <td>145.2</td>
      <td>1</td>
      <td>31.0</td>
      <td>33.1</td>
      <td>36.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>63.7</td>
      <td>147.9</td>
      <td>2</td>
      <td>26.0</td>
      <td>34.0</td>
      <td>31.5</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>105.9</td>
      <td>157.7</td>
      <td>10</td>
      <td>29.2</td>
      <td>35.0</td>
      <td>40.7</td>
      <td>129.1</td>
    </tr>
    <tr>
      <th>e</th>
      <td>77.5</td>
      <td>148.3</td>
      <td>10</td>
      <td>30.5</td>
      <td>34.0</td>
      <td>34.4</td>
      <td>107.6</td>
    </tr>
  </tbody>
</table>
</div>


