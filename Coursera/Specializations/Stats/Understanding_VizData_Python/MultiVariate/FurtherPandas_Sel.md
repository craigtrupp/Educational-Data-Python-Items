
## Unit Testing
While we will not cover the [unit testing library](https://docs.python.org/3/library/unittest.html) that python has, we wanted to introduce you to a simple way that you can test your code.

Unit testing is important because it the only way you can be sure that your code is do what you think it is doing. 

Remember, just because ther are no errors does not mean your code is correct.


```python
import numpy as np
import pandas as pd
import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
```


```python
# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")
df.index = range(1,df.shape[0]+1) # range not inclusive at end so add 1
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
      <th>1</th>
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
      <th>2</th>
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
      <th>3</th>
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
      <th>4</th>
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
      <th>5</th>
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



### Goal
We want to find the mean of first 100 rows of 'BPXSY1' when 'RIDAGEYR' > 60


```python
# One possible way of doing this is:
print(pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,100), 'BPXSY1'])) # this captures nulls ... not great
# Current version of python will include this warning, older versions will not
age_60 = df['RIDAGEYR'] > 60
display(df.loc[age_60, ['BPXSY1', 'RIDAGEYR']].head(100)['BPXSY1'].mean()) # this would be how I do it 136.29
# display(df[df.RIDAGEYR > 60].loc[range(0,10), ['BPXSY1', 'RIDAGEYR']])
display(df.loc[df['RIDAGEYR'] > 60, ['BPXSY1', 'RIDAGEYR']].head(10))
```

    139.57142857142858



    136.29166666666666



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
      <th>BPXSY1</th>
      <th>RIDAGEYR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>128.0</td>
      <td>62</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.0</td>
      <td>78</td>
    </tr>
    <tr>
      <th>6</th>
      <td>116.0</td>
      <td>72</td>
    </tr>
    <tr>
      <th>14</th>
      <td>124.0</td>
      <td>67</td>
    </tr>
    <tr>
      <th>15</th>
      <td>132.0</td>
      <td>67</td>
    </tr>
    <tr>
      <th>22</th>
      <td>148.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>23</th>
      <td>140.0</td>
      <td>69</td>
    </tr>
    <tr>
      <th>30</th>
      <td>122.0</td>
      <td>68</td>
    </tr>
    <tr>
      <th>31</th>
      <td>146.0</td>
      <td>69</td>
    </tr>
    <tr>
      <th>32</th>
      <td>160.0</td>
      <td>66</td>
    </tr>
  </tbody>
</table>
</div>



```python
# test our code on only ten rows so we can easily check
test = pd.DataFrame({'col1': np.repeat([3,1],5), 'col2': range(3,13)}, index=range(1,11))
test
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
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
# pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,5), 'BPXSY1'])
# should return 5

pd.Series.mean(test[test.col1 > 2].loc[range(0,5), 'col2'])
```




    4.5



What went wrong?


```python
test[test.col1 > 2].loc[range(0,5), 'col2']
# 0 is not in the row index labels because the second row's value is < 2. For now, pandas defaults to filling this
# with NaN
```




    0    NaN
    1    3.0
    2    4.0
    3    5.0
    4    6.0
    Name: col2, dtype: float64




```python
# Using the .iloc method instead, we are correctly choosing the first 5 rows, regardless of their row labels
test[test.col1 >2].iloc[range(0,5), 1]
```




    1    3
    2    4
    3    5
    4    6
    5    7
    Name: col2, dtype: int64




```python
pd.Series.mean(test[test.col1 >2].iloc[range(0,5), 1])
```


```python
# We can compare what our real dataframe looks like with the incorrect and correct methods
df[df.RIDAGEYR > 60].loc[range(0,5), :] # Filled with NaN whenever a row label does not meet the condition
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>83732.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>62.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>134671.37</td>
      <td>1.0</td>
      <td>125.0</td>
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
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>83734.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>78.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>12400.01</td>
      <td>1.0</td>
      <td>131.0</td>
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
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df.RIDAGEYR > 60].iloc[range(0,5), :] # Correct picks the first fice rows such that 'RIDAGEYR" > 60
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
      <th>1</th>
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
      <th>3</th>
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
      <th>6</th>
      <td>83737</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>72</td>
      <td>1</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5</td>
      <td>11252.31</td>
      <td>1</td>
      <td>128</td>
      <td>2.82</td>
      <td>116.0</td>
      <td>58.0</td>
      <td>122.0</td>
      <td>58.0</td>
      <td>64.4</td>
      <td>150.0</td>
      <td>28.6</td>
      <td>34.4</td>
      <td>33.5</td>
      <td>31.4</td>
      <td>92.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>83754</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>67</td>
      <td>2</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>7</td>
      <td>10495.87</td>
      <td>1</td>
      <td>128</td>
      <td>0.89</td>
      <td>124.0</td>
      <td>76.0</td>
      <td>116.0</td>
      <td>64.0</td>
      <td>117.8</td>
      <td>164.1</td>
      <td>43.7</td>
      <td>34.8</td>
      <td>38.6</td>
      <td>42.7</td>
      <td>123.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>83755</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>2</td>
      <td>1</td>
      <td>67</td>
      <td>4</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>14080.10</td>
      <td>1</td>
      <td>126</td>
      <td>2.04</td>
      <td>132.0</td>
      <td>84.0</td>
      <td>136.0</td>
      <td>82.0</td>
      <td>97.4</td>
      <td>183.8</td>
      <td>28.8</td>
      <td>42.5</td>
      <td>40.6</td>
      <td>34.2</td>
      <td>106.3</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Applying the correct method to the original question about BPXSY1
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), 16]))

# Another way to reference the BPXSY1 variable
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), df.columns.get_loc('BPXSY1')]))
```

    136.29166666666666
    136.29166666666666

