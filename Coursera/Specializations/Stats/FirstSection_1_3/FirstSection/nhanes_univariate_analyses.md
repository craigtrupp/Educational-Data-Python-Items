
## Univariate data analyses - NHANES case study

Here we will demonstrate how to use Python and [Pandas](https://pandas.pydata.org/) to perform some basic analyses with univariate data, using the 2015-2016 wave of the [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) study to illustrate the techniques.

The following import statements make the libraries that we will need available.  Note that in a Jupyter notebook, you should generally use the `%matplotlib inline` directive, which would not be used when running a script outside of the Jupyter environment.


```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

Next we will load the NHANES data from a file.


```python
da = pd.read_csv("nhanes_2015_2016.csv")
```

### Frequency tables

The [value_counts](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) method can be used to determine the number of times that each distinct value of a variable occurs in a data set.  In statistical terms, this is the "frequency distribution" of the variable.  Below we show the frequency distribution of the [DMDEDUC2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2) variable, which is a variable that reflects a person's level of educational attainment.  The `value_counts` method produces a table with two columns.  The first column contains all distinct observed values for the variable.  The second column contains the number of times each of these values occurs.  Note that the table returned by `value_counts` is actually a Pandas data frame, so can be further processed using any Pandas methods for working with data frames.

The numbers 1, 2, 3, 4, 5, 9 seen below are integer codes for the 6 possible non-missing values of the DMDEDUC2 variable.  The meaning of these codes is given in the NHANES codebook located [here](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2), and will be discussed further below.  This table shows, for example, that 1621 people in the data file have DMDEDUC=4, which indicates that the person has completed some college, but has not graduated with a four-year degree.


```python
da.DMDEDUC2.value_counts()
```




    4.0    1621
    5.0    1366
    3.0    1186
    1.0     655
    2.0     643
    9.0       3
    Name: DMDEDUC2, dtype: int64



Note that the `value_counts` method excludes missing values.  We confirm this below by adding up the number of observations with a DMDEDUC2 value equal to 1, 2, 3, 4, 5, or 9 (there are 5474 such rows), and comparing this to the total number of rows in the data set, which is 5735. This tells us that there are 5735 - 5474 = 261 missing values for this variable (other variables may have different numbers of missing values).


```python
print(da.DMDEDUC2.value_counts().sum())
print(1621 + 1366 + 1186 + 655 + 643 + 3) # Manually sum the frequencies
print(da.shape)
```

    5474
    5474
    (5735, 28)


Another way to obtain this result is to locate all the null (missing) values in the data set using the [isnull](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.isnull.html) Pandas function, and count the number of such locations.


```python
print(pd.isnull(da.DMDEDUC2).sum()) # particular column
# across the whole dataframe
display(da.isna().sum()) # We see the null/empty values across each of our columns too
```

    261



    SEQN           0
    ALQ101       527
    ALQ110      4004
    ALQ130      2356
    SMQ020         0
    RIAGENDR       0
    RIDAGEYR       0
    RIDRETH1       0
    DMDCITZN       1
    DMDEDUC2     261
    DMDMARTL     261
    DMDHHSIZ       0
    WTINT2YR       0
    SDMVPSU        0
    SDMVSTRA       0
    INDFMPIR     601
    BPXSY1       334
    BPXDI1       334
    BPXSY2       200
    BPXDI2       200
    BMXWT         69
    BMXHT         62
    BMXBMI        73
    BMXLEG       390
    BMXARML      308
    BMXARMC      308
    BMXWAIST     367
    HIQ210      1003
    dtype: int64


In some cases it is useful to [replace](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.replace.html) integer codes with a text label that reflects the code's meaning.  Below we create a new variable called 'DMDEDUC2x' that is recoded with text labels, then we generate its frequency distribution.


```python
display(da['DMDEDUC2'].value_counts())# reminder of the value_counts
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know"})
da.DMDEDUC2x.value_counts()
# Notice our new columns not has a categorical type string value for it's value_counts now 
```


    4.0    1621
    5.0    1366
    3.0    1186
    1.0     655
    2.0     643
    9.0       3
    Name: DMDEDUC2, dtype: int64





    Some college/AA    1621
    College            1366
    HS/GED             1186
    <9                  655
    9-11                643
    Don't know            3
    Name: DMDEDUC2x, dtype: int64



We will also want to have a relabeled version of the gender variable, so we will construct that now as well.  We will follow a convention here of appending an 'x' to the end of a categorical variable's name when it has been recoded from numeric to string (text) values.


```python
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
```

For many purposes it is more relevant to consider the proportion of the sample with each of the possible category values, rather than the number of people in each category.  We can do this as follows:


```python
x = da.DMDEDUC2x.value_counts()  # x is just a name to hold this value temporarily
x / x.sum() # The series return for the column value counts has the (Distribution Amount out of 1) with the division for each value_count
```




    Some college/AA    0.296127
    College            0.249543
    HS/GED             0.216661
    <9                 0.119657
    9-11               0.117464
    Don't know         0.000548
    Name: DMDEDUC2x, dtype: float64



In some cases we will want to treat the missing response category as another category of observed response, rather than ignoring it when creating summaries.  Below we create a new category called "Missing", and assign all missing values to it usig [fillna](https://pandas.pydata.org/pandas-docs/stable/missing_data.html#filling-missing-values-fillna).  Then we recalculate the frequency distribution.  We see that 4.6% of the responses are missing.


```python
da["DMDEDUC2x"] = da.DMDEDUC2x.fillna("Missing")
x = da.DMDEDUC2x.value_counts()
x / x.sum()
```




    Some college/AA    0.282650
    College            0.238187
    HS/GED             0.206800
    <9                 0.114211
    9-11               0.112119
    Missing            0.045510
    Don't know         0.000523
    Name: DMDEDUC2x, dtype: float64



### Numerical summaries

A quick way to get a set of numerical summaries for a quantitative variable is with the [describe](https://pandas.pydata.org/pandas-docs/stable/basics.html#summarizing-data-describe) data frame method.  Below we demonstrate how to do this using the body weight variable ([BMXWT](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXWT)).  As with many surveys, some data values are missing, so we explicitly drop the missing cases using the [dropna](https://pandas.pydata.org/pandas-docs/stable/missing_data.html#dropping-axis-labels-with-missing-data-dropna) method before generating the summaries.


```python
da.BMXWT.dropna().describe()
```




    count    5666.000000
    mean       81.342676
    std        21.764409
    min        32.400000
    25%        65.900000
    50%        78.200000
    75%        92.700000
    max       198.900000
    Name: BMXWT, dtype: float64



It's also possible to calculate individual summary statistics from one column of a data set.  This can be done using Pandas methods, or with numpy functions:


```python
x = da.BMXWT.dropna()  # Extract all non-missing values of BMXWT into a variable called 'x'
print(x.mean()) # Pandas method
print(np.mean(x)) # Numpy function
print(da.BMXWT.mean()) # Series Mean function (it's ignoring nulls on default)

print(x.median(), da['BMXWT'].median()) # Median a Series method too
print(np.percentile(x, 50))  # 50th percentile, same as the median
print(np.percentile(x, 75))  # 75th percentile
print(x.quantile(0.75)) # Pandas method for quantiles, equivalent to 75th percentile
```

    81.34267560889516
    81.34267560889516
    81.34267560889516
    78.2 78.2
    78.2
    92.7
    92.7


Next we look at frequencies for a systolic blood pressure measurement ([BPXSY1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY1)).  "BPX" here is the NHANES prefix for blood pressure measurements, "SY" stands for "systolic" blood pressure (blood pressure at the peak of a heartbeat cycle), and "1" indicates that this is the first of three systolic blood presure measurements taken on a subject.

A person is generally considered to have pre-hypertension when their systolic blood pressure is between 120 and 139, or their diastolic blood pressure is between 80 and 89.  Considering only the systolic condition, we can calculate the proprotion of the NHANES sample who would be considered to have pre-hypertension. 


```python
round(np.mean((da.BPXSY1 >= 120) & (da.BPXSY2 <= 139)), 5)  # "&" means "and" we can calculate the proprotion of the NHANES sample
```




    0.37419



Next we calculate the propotion of NHANES subjects who are pre-hypertensive based on diastolic blood pressure.


```python
round(np.mean((da.BPXDI1 >= 80) & (da.BPXDI2 <= 89)), 5)
```




    0.14804



Finally we calculate the proportion of NHANES subjects who are pre-hypertensive based on either systolic or diastolic blood pressure.  Since some people are pre-hypertensive under both criteria, the proportion below is less than the sum of the two proportions calculated above.

Since the combined systolic and diastolic condition for pre-hypertension is somewhat complex, below we construct temporary variables 'a' and 'b' that hold the systolic and diastolic pre-hypertensive status separately, then combine them with a "logical or" to obtain the final status for each subject.


```python
a = (da.BPXSY1 >= 120) & (da.BPXSY2 <= 139)
b = (da.BPXDI1 >= 80) & (da.BPXDI2 <= 89)
print(type(a), type(b), len(a), len(b), '\n\n') # Each is a boolean series return for the rows if the condition is true for a or b cond 
print('How do our systolic pre-hypertensive values sit based on the condition defined in variable a?', '\n') 
print(a.value_counts(), '\n')

## pre-hypertension when their systolic blood pressure is between 120 and 139 (Let's dig into how a is getting the proportion)
a_no = a.value_counts(ascending=False).iloc[0] # target the yes and no of one of the types (we'll do A to confirm the mean above of rows that fit our condition)
print("The account in the boolean series for a that is not true (first row in series return of value_counts) : {}".format(a_no))
a_yes = a.value_counts(ascending=False).iloc[1]
print("The account in the boolean series for a that IS TRUE (second row in series return of value_counts) : {}".format(a_yes))

print('\n')

## To get the proportion we can divide our series True matches by the Series Total (True / (True + False) - we'll format the proportion in the string below)
print("Our sample set proprition considered to have pre-hypertension (Sys >= 120 && Sys <= 139) is : {:.5f}".format(a_yes/(a_yes + a_no))) # This matches our value above for the initial condition! Know how that's working now

## Nice this matches our cell slightly above where the mean function on numpy is used to get the proportion!

print('\n')

# We'll get the count of the Series/Df['column'] to confirm the total counts ... now does that include nulls?
print('Do our totals for each condition match the count of the series/df[column]? {}, is our two condition counts summed. {}, is our series (dframe) column total count. They do! Any null potential issues though?'.format(a_yes + a_no, da['BPXSY1'].shape[0]), 'Total null count for \ncolumn (BPXSY1) : {}.'.format(da['BPXSY1'].isna().sum()),
      'Our total values for the conditional check should omit nulls and check a sum of our column sum (initial output of this statement) of valid values')

print('\n')

## Let's create a new series from the column and drop the nulls and take a look
sep_series_sys = da['BPXSY1'].dropna()
print("Our total count for values in the new series w/o nulls is : {}".format(len(sep_series_sys)))

## We can use np.mean to get a proporition for the same type condition on our new series
print("Our proportion considered to have pre-hypertension from our Values with null values removed : {:.5f}".format(np.mean((sep_series_sys >= 120) & (sep_series_sys <= 139))))

## Food for thought
print("We see the proportion is different by about 1.5% in terms of the conditional check. The null values have influenced \nour proportion that were labeled 'False' by both the numpy method and value_counts method on series/column")

print('\n')

print("Good to flesh out the above in terms of identifying if the proprotion we're seeking is influence by our data. \nLet's see how our conditions fit the whole distribution as is (with the caveat we know we have a margin of error \nbased on null values)")

print('\n')

## This combines both our conditions : Since some people are pre-hypertensive under both criteria, the proportion below is less than the sum of the two proportions calculated above.
print("Using the pipe (or) operator we see the combined proportion of {:.5f} fitting either condition (and not double counting True values for both conditions so not a summation of both individual proprotions in the above cells)".format(round(np.mean(a | b), 5)),
     "Great! We \nsee that indeed a chunk fits both our conditions.") # "|" means "or"


## Can we get it ourselves?
print('\n')

print("How would we get it ourselves? What's our index look like .. wait do we have an index? What type are we working with for our proportions above? Oh that's right they're series (top of the page refresher). Well what's they're respective index values")

print('\n')

print("Our type indexes for each series are [systolic_pre-hypertensive condition : {}, \ndiastolic_pre-hypertensive condition : {}]".format(a.index, b.index))
print("AAaaah we see it's just a range index with the same length (same dataframe). We should be able to not double count \nany same index and get a similar proportion!")

print('\n')

# we can use a tuple to remove duplicates! (We can use the series' values property to more easily iterate)
print("We can iterate through a series' values by : a[:5].values which produces : {}".format(a[:5].values), "We'll also need to get the index though to find duplicates! Let's see if we can get the index from a condition")
print("Now we can get a series ... from our series by subsetting the boolean condition series a as such : a[a == True]",
      "Let's confirm the type as : {}".format(type(a[a == True])), "We can convert this condition's returns and targe their unique index like : a[a == True].index.tolist(). A df.head() type return (5 records) shows the first five indexes that are true for the series! {}".format(a[a == True].index.tolist()[:5]))

print('\n')

a_true_cond_idx = a[a == True].index.tolist() # We can get the index int value from our boolean series like such and capture the unique index where the Series value is True
b_true_cond_idx = b[b == True].index.tolist()


a_b_combined_true = a_true_cond_idx + b_true_cond_idx  # We Concatenate the lists (Could Extend as well) (See Below!)
a_b_combined_extend = a_true_cond_idx.copy()
a_b_combined_extend.extend(b_true_cond_idx)

# alternative way to combine each list. Do they match? ... They do!  Are they the same ... They are!
print("Our concatenated list of the two indexes has a length of : {}. Our use of the .extend method also has the same \nlength of : {}. We can check if they are equal by list_a == list_b which returns : {}".format(len(a_b_combined_true), len(a_b_combined_extend), a_b_combined_true == a_b_combined_extend))

print('\n')

# Put it together now by making a unique set of our indexes and dividing by the total to check the proportion of abour 44% - 0.43976 value of the pipe np.mean
a_b_combined_unique = list(set(a_b_combined_true)) # we can remove duplicate indexes as such
print("After getting just unique indexes through assignment as : list(set(combined_list)). We get a value of {}. Which \nrepresents our total unique true rows for either condition".format(len(a_b_combined_unique)))

print('\n')

print("We check the proportion from gathering our own unique combined count : {:.5f}".format(len(a_b_combined_unique)/len(a))) # len(a) here just the boolean series counting all values for the column

print("We see that the values match!")
```

    <class 'pandas.core.series.Series'> <class 'pandas.core.series.Series'> 5735 5735 
    
    
    How do our systolic pre-hypertensive values sit based on the condition defined in variable a? 
    
    False    3589
    True     2146
    dtype: int64 
    
    The account in the boolean series for a that is not true (first row in series return of value_counts) : 3589
    The account in the boolean series for a that IS TRUE (second row in series return of value_counts) : 2146
    
    
    Our sample set proprition considered to have pre-hypertension (Sys >= 120 && Sys <= 139) is : 0.37419
    
    
    Do our totals for each condition match the count of the series/df[column]? 5735, is our two condition counts summed. 5735, is our series (dframe) column total count. They do! Any null potential issues though? Total null count for 
    column (BPXSY1) : 334. Our total values for the conditional check should omit nulls and check a sum of our column sum (initial output of this statement) of valid values
    
    
    Our total count for values in the new series w/o nulls is : 5401
    Our proportion considered to have pre-hypertension from our Values with null values removed : 0.38956
    We see the proportion is different by about 1.5% in terms of the conditional check. The null values have influenced 
    our proportion that were labeled 'False' by both the numpy method and value_counts method on series/column
    
    
    Good to flesh out the above in terms of identifying if the proprotion we're seeking is influence by our data. 
    Let's see how our conditions fit the whole distribution as is (with the caveat we know we have a margin of error 
    based on null values)
    
    
    Using the pipe (or) operator we see the combined proportion of 0.43976 fitting either condition (and not double counting True values for both conditions so not a summation of both individual proprotions in the above cells) Great! We 
    see that indeed a chunk fits both our conditions.
    
    
    How would we get it ourselves? What's our index look like .. wait do we have an index? What type are we working with for our proportions above? Oh that's right they're series (top of the page refresher). Well what's they're respective index values
    
    
    Our type indexes for each series are [systolic_pre-hypertensive condition : RangeIndex(start=0, stop=5735, step=1), 
    diastolic_pre-hypertensive condition : RangeIndex(start=0, stop=5735, step=1)]
    AAaaah we see it's just a range index with the same length (same dataframe). We should be able to not double count 
    any same index and get a similar proportion!
    
    
    We can iterate through a series' values by : a[:5].values which produces : [ True False  True  True False] We'll also need to get the index though to find duplicates! Let's see if we can get the index from a condition
    Now we can get a series ... from our series by subsetting the boolean condition series a as such : a[a == True] Let's confirm the type as : <class 'pandas.core.series.Series'> We can convert this condition's returns and targe their unique index like : a[a == True].index.tolist(). A df.head() type return (5 records) shows the first five indexes that are true for the series! [0, 2, 3, 7, 13]
    
    
    Our concatenated list of the two indexes has a length of : 2995. Our use of the .extend method also has the same 
    length of : 2995. We can check if they are equal by list_a == list_b which returns : True
    
    
    After getting just unique indexes through assignment as : list(set(combined_list)). We get a value of 2522. Which 
    represents our total unique true rows for either condition
    
    
    We check the proportion from gathering our own unique combined count : 0.43976


Blood pressure measurements are affected by a phenomenon called "white coat anxiety", in which a subject's bood pressure may be slightly elevated if they are nervous when interacting with health care providers.  Typically this effect subsides if the blood pressure is measured several times in sequence.  In NHANES, both systolic and diastolic blood pressure are meausred three times for each subject (e.g. [BPXSY2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY2) is the second measurement of systolic blood pressure).  We can calculate the extent to which white coat anxiety is present in the NHANES data by looking a the mean difference between the first two systolic or diastolic blood pressure measurements.


```python
print((da.BPXSY1 - da.BPXSY2)[:5], '\n') # Just a series of arithmetic operations for each series prior to getting the average
# Can get our own mean to check
sys_dif = da.BPXSY1 - da.BPXSY2
sys_dif_mean = sys_dif.sum() / len(sys_dif)
print('Series method mean Series.mean() : {}'.format(sys_dif.mean()))

print(np.mean(da.BPXSY1 - da.BPXSY2))
print(np.mean(da.BPXDI1 - da.BPXDI2))

# sr = pd.Series([10, 25, 3, 25, 24, 6])
# print(sr.mean(), sr.sum()/len(sr)) # 15.5 15.5
```

    0     4.0
    1     6.0
    2     6.0
    3    -2.0
    4   -14.0
    dtype: float64 
    
    Series method mean Series.mean() : 0.6749860309182343
    0.6749860309182343
    0.3490407897187558


### Graphical summaries

Quantitative variables can be effectively summarized graphically.  Below we see the distribution of body weight (in Kg), shown as a histogram.  It is evidently right-skewed.


```python
sns.distplot(da.BMXWT.dropna())
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f69ec4afdd8>




![png](Images/output_32_1.png)


Next we look at the histogram of systolic blood pressure measurements.  You can see that there is a tendency for the measurements to be rounded to the nearest 5 or 10 units.


```python
sns.distplot(da.BPXSY1.dropna())
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f69ec4af5f8>




![png](Images/output_34_1.png)


To compare several distributions, we can use side-by-side boxplots.  Below we compare the distributions of the first and second systolic blood pressure measurements (BPXSY1, BPXSY2), and the first and second diastolic blood pressure measurements ([BPXDI1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXDI1), BPXDI2). As expected, diastolic measurements are substantially lower than systolic measurements.  Above we saw that the second blood pressure reading on a subject tended on average to be slightly lower than the first measurement.  This difference was less than 1 mm/Hg, so is not visible in the "marginal" distributions shown below.


```python
bp = sns.boxplot(data=da.loc[:, ["BPXSY1", "BPXSY2", "BPXDI1", "BPXDI2"]])
bp.set_ylabel("Blood pressure in mm/Hg")
bp
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f69ea307978>




![png](Images/output_36_1.png)


### Stratification

One of the most effective ways to get more information out of a dataset is to divide it into smaller, more uniform subsets, and analyze each of these "strata" on its own.  We can then formally or informally compare the findings in the different strata.  When working with human subjects, it is very common to stratify on demographic factors such as age, sex, and race.

To illustrate this technique, consider blood pressure, which is a value that tends to increase with age.  To see this trend in the NHANES data, we can [partition](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html) the data into age strata, and construct side-by-side boxplots of the systolic blood pressure (SBP) distribution within each stratum.  Since age is a quantitative variable, we need to create a series of "bins" of similar SBP values in order to stratify the data.  Each box in the figure below is a summary of univariate data within a specific population stratum (here defined by age).


```python
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) # Create age strata based on these cut points (pandas cut)
plt.figure(figsize=(12, 5))  # Make the figure wider than default (12cm wide by 5cm tall)
sns.boxplot(x="agegrp", y="BPXSY1", data=da)  # Make boxplot of BPXSY1 stratified by age group
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f8388799ef0>




![png](Images/output_38_1.png)


Taking this a step further, it is also the case that blood pressure tends to differ between women and men.  While we could simply make two side-by-side boxplots to illustrate this contrast, it would be a bit odd to ignore age after already having established that it is strongly associated with blood pressure.  Therefore, we will doubly stratify the data by gender and age.

We see from the figure below that within each gender, older people tend to have higher blood pressure than younger people.  However within an age band, the relationship between gender and systolic blood pressure is somewhat complex -- in younger people, men have substantially higher blood pressures than women of the same age.  However for people older than 50, this relationship becomes much weaker, and among people older than 70 it appears to reverse. It is also notable that the variation of these distributions, reflected in the height of each box in the boxplot, increases with age.


```python
print(type(a_b_combined_true)) # <class 'list'> ... well a variable from an above cell returns but I guess the column doesn't
## da["agegrp"] was set in the cell above checking if it's still there
print([x for x in da.columns.tolist() if x[0].lower() == 'a']) # agegrp (notably not here) so it's duplicated in this cell
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) 
plt.figure(figsize=(12, 5))
sns.boxplot(x="agegrp", y="BPXSY1", hue="RIAGENDRx", data=da) # Hue parameter a second categorical argument to use
```

    <class 'list'>
    ['ALQ101', 'ALQ110', 'ALQ130']





    <matplotlib.axes._subplots.AxesSubplot at 0x7f69ea12fef0>




![png](Images/output_40_2.png)


When stratifying on two factors (here age and gender), we can group the boxes first by age, and within age bands by gender, as above, or we can do the opposite -- group first by gender, and then within gender group by age bands.  Each approach highlights a different aspect of the data.


```python
da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="RIAGENDRx", y="BPXSY1", hue="agegrp", data=da)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f69ea307780>




![png](Images/output_42_1.png)


Stratification can also be useful when working with categorical variables.  Below we look at the frequency distribution of educational attainment ("DMDEDUC2") within 10-year age bands.  While "some college" is the most common response in all age bands, up to around age 60 the second most common response is "college" (i.e. the person graduated from college with a four-year degree). However for people over 50, there are as many or more people with only high school or general equivalency diplomas (HS/GED) than there are college graduates. 

**Note on causality and confounding:** An important role of statistics is to aid researchers in identifying causes underlying observed differences.  Here we have seen differences in both blood pressure and educational attainment based on age.  It is plausible that aging directly causes blood pressure to increase.  But in the case of educational attainment, this is actually a "birth cohort effect".  NHANES is a cross sectional survey (all data for one wave were collected at a single point in time). People who were, say, 65 in 2015 (when these data were collected), were college-aged around 1970, while people who were in their 20's in 2015 were college-aged in around 2010 or later.  Over the last few decades, it has become much more common for people to at least begin a college degree than it was in the past.  Therefore, younger people as a group have higher educational attainment than older people as a group.  As these young people grow older, the cross sectional relationship between age and educational attainment will change.


```python
# groupby the age buckets and select that subset's unique counts for the following column
# Syntax : df.groupby('groupbycolumn')['TargetColumnValuesforGroupSubsets'].aggfunc()   ## Can also multi-level group with a list to groupby method
da.groupby("agegrp")["DMDEDUC2x"].value_counts() 
```




    agegrp    DMDEDUC2x      
    (18, 30]  Some college/AA    364
              College            278
              HS/GED             237
              Missing            128
              9-11                99
              <9                  47
    (30, 40]  Some college/AA    282
              College            264
              HS/GED             182
              9-11               111
              <9                  93
    (40, 50]  Some college/AA    262
              College            260
              HS/GED             171
              9-11               112
              <9                  98
    (50, 60]  Some college/AA    258
              College            220
              HS/GED             220
              9-11               122
              <9                 104
    (60, 70]  Some college/AA    238
              HS/GED             192
              College            188
              <9                 149
              9-11               111
    (70, 80]  Some college/AA    217
              HS/GED             184
              <9                 164
              College            156
              9-11                88
              Don't know           3
    Name: DMDEDUC2x, dtype: int64



We can also stratify jointly by age and gender to explore how educational attainment varies by both of these factors simultaneously.  In doing this, it is easier to interpret the results if we [pivot](https://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-by-stacking-and-unstacking) the education levels into the columns, and normalize the counts so that they sum to 1.  After doing this, the results can be interpreted as proportions or probabilities.  One notable observation from this table is that for people up to age around 60, women are more likely to have graduated from college than men, but for people over aged 60, this relationship reverses.


```python
dx = da.loc[~da.DMDEDUC2x.isin(["Don't know", "Missing"]), :]  # Eliminate rare/missing values
# Syntax for exclusion with .loc : dframe.loc[-dframe['column'] == 'value'] (This will target all rows in the frame not equal to the condition)
dx = dx.groupby(["agegrp", "RIAGENDRx"])["DMDEDUC2x"]
dx = dx.value_counts()
print(dx[:10]) # Subset of groupedby value_counts for categorical value of interest DMDEDUC2x
# dx = dx.unstack() # Restructure the results from 'long' to 'wide'
# dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
# print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal places
```

    agegrp    RIAGENDRx  DMDEDUC2x      
    (18, 30]  Female     Some college/AA    207
                         College            156
                         HS/GED             119
                         9-11                44
                         <9                  27
              Male       Some college/AA    157
                         College            122
                         HS/GED             118
                         9-11                55
                         <9                  20
    Name: DMDEDUC2x, dtype: int64



```python
dx = dx.unstack() # Restructure the results from 'long' to 'wide'
#print(dx[:5]) # Note here how the value_counts have been set as column values for each group that has a multi-level index for the groupig

dx_cp = dx[:5].copy()
#dx_cp['Total'] = dx_cp.apply(lambda x: x.sum(), axis=1)
display(dx_cp)
print('\n')
## Normalize a copy ... of our copy (Female (18,30) row total = 553) first value in dis
dx_cp_one = dx_cp[:2].copy()
dx_cp_one = dx_cp_one.apply(lambda x: x/x.sum(), axis=1)
display(dx_cp_one) # first value in display for the normalized value for females is 44 / 553 =  0.07956 (553 = 44 + 27 + 156 + 119 + 207)

print('\n')

## Now that we see a small sample of what's to come we can perform across the whole dataset to get a proprotion
## The lambda function is being performed across each row (1 Male Row & 1 Female Row) for each outer groupby column (agegrp buckets)
## The Function takes each column value for the male/female row per group and divides the row value minus the row total to get a percentage 
## This percentage signifies the proportion for that row column value against all total for the same "strata" or partitioned row 

dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
display(dx[:5])

print('\n\n')

print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal places


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
      <th>DMDEDUC2x</th>
      <th>9-11</th>
      <th>&lt;9</th>
      <th>College</th>
      <th>HS/GED</th>
      <th>Some college/AA</th>
    </tr>
    <tr>
      <th>agegrp</th>
      <th>RIAGENDRx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">(18, 30]</th>
      <th>Female</th>
      <td>44</td>
      <td>27</td>
      <td>156</td>
      <td>119</td>
      <td>207</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>55</td>
      <td>20</td>
      <td>122</td>
      <td>118</td>
      <td>157</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">(30, 40]</th>
      <th>Female</th>
      <td>42</td>
      <td>46</td>
      <td>149</td>
      <td>78</td>
      <td>159</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>69</td>
      <td>47</td>
      <td>115</td>
      <td>104</td>
      <td>123</td>
    </tr>
    <tr>
      <th>(40, 50]</th>
      <th>Female</th>
      <td>55</td>
      <td>53</td>
      <td>150</td>
      <td>87</td>
      <td>157</td>
    </tr>
  </tbody>
</table>
</div>


    
    



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
      <th>DMDEDUC2x</th>
      <th>9-11</th>
      <th>&lt;9</th>
      <th>College</th>
      <th>HS/GED</th>
      <th>Some college/AA</th>
    </tr>
    <tr>
      <th>agegrp</th>
      <th>RIAGENDRx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">(18, 30]</th>
      <th>Female</th>
      <td>0.079566</td>
      <td>0.048825</td>
      <td>0.282098</td>
      <td>0.21519</td>
      <td>0.374322</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>0.116525</td>
      <td>0.042373</td>
      <td>0.258475</td>
      <td>0.25000</td>
      <td>0.332627</td>
    </tr>
  </tbody>
</table>
</div>


    
    



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
      <th>DMDEDUC2x</th>
      <th>9-11</th>
      <th>&lt;9</th>
      <th>College</th>
      <th>HS/GED</th>
      <th>Some college/AA</th>
    </tr>
    <tr>
      <th>agegrp</th>
      <th>RIAGENDRx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">(18, 30]</th>
      <th>Female</th>
      <td>0.079566</td>
      <td>0.048825</td>
      <td>0.282098</td>
      <td>0.215190</td>
      <td>0.374322</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>0.116525</td>
      <td>0.042373</td>
      <td>0.258475</td>
      <td>0.250000</td>
      <td>0.332627</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">(30, 40]</th>
      <th>Female</th>
      <td>0.088608</td>
      <td>0.097046</td>
      <td>0.314346</td>
      <td>0.164557</td>
      <td>0.335443</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>0.150655</td>
      <td>0.102620</td>
      <td>0.251092</td>
      <td>0.227074</td>
      <td>0.268559</td>
    </tr>
    <tr>
      <th>(40, 50]</th>
      <th>Female</th>
      <td>0.109562</td>
      <td>0.105578</td>
      <td>0.298805</td>
      <td>0.173307</td>
      <td>0.312749</td>
    </tr>
  </tbody>
</table>
</div>


    
    
    
    DMDEDUC2x           9-11    <9  College  HS/GED  Some college/AA
    agegrp   RIAGENDRx                                              
    (18, 30] Female    0.080 0.049    0.282   0.215            0.374
             Male      0.117 0.042    0.258   0.250            0.333
    (30, 40] Female    0.089 0.097    0.314   0.165            0.335
             Male      0.151 0.103    0.251   0.227            0.269
    (40, 50] Female    0.110 0.106    0.299   0.173            0.313
             Male      0.142 0.112    0.274   0.209            0.262
    (50, 60] Female    0.117 0.102    0.245   0.234            0.302
             Male      0.148 0.123    0.231   0.242            0.256
    (60, 70] Female    0.118 0.188    0.195   0.206            0.293
             Male      0.135 0.151    0.233   0.231            0.249
    (70, 80] Female    0.105 0.225    0.149   0.240            0.281
             Male      0.113 0.180    0.237   0.215            0.255

