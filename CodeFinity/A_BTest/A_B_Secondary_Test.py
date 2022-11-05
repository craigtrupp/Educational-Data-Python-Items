#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:11:50 2022

@author: craigrupp
"""

import pandas as pd 

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/1e089012-bfcf-4d61-9ac9-bb649ece39f2/abtest.csv')


# Save only 'Web' platform into the new df
df_platform = df.query('platform == "Web" ')

# Save the information fixed only after the '2021-01-10'
df_ab = df_platform.query('date > "2021-01-10" ')

# Show the data
print(df_ab.head())


## Chose Criterion : Evaluate Distribution for Test Determination
import seaborn as sns
# Import the scipy
import scipy
# Import the statsmodels.api
import statsmodels.api as sm

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/1e089012-bfcf-4d61-9ac9-bb649ece39f2/abtest_with_changes.csv')

# Build the distplot
sns.distplot(df.contact_views_number)
# Build the qqplot
sm.qqplot(df.contact_views_number, line = 's')

# Perform the normaltest
print(scipy.stats.normaltest(df.contact_views_number)) 

## Non Normal Test Result Return
# =============================================================================
# # NormaltestResult(statistic=568863.9375989069, pvalue=0.0)
# # 0.00 < 0.05 => the distribution isn't normal.
# =============================================================================



## As such : We'll use the Mann-Whitney criterion in our A/B test.
## This is chosen as the two groups being chosen are independent and the Distribution is not normal based on the column's return value for the test above 


## First We Need to Divide Into Groups
# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/1e089012-bfcf-4d61-9ac9-bb649ece39f2/abtest_with_changes.csv')
print(df.columns.tolist(), df.shape)
print(df['group'].value_counts())
# Create the new variable df_control with the 'control' group
df_control = df.query('group == "control" ')
# Create the new variable df_test with the 'test' group
df_test = df.query('group == "test"')

# Show the first row of the df_control
print(df_control.head(1))
# Show the first row of the df_test
print(df_test.head(1))


## Comparing Groups
# =============================================================================
# Let's try to build the qqplot for this test. 
# Furthermore, in this chapter, we will compare the confidence intervals of groups.
# =============================================================================

# Build the qqplot for the df_control
sm.qqplot(df_control.contact_views_number, line = 's')
# Build the qqplot for the df_test
sm.qqplot(df_test.contact_views_number, line = 's')

# Building the interval for the df_control
print(scipy.stats.t.interval(0.95, df_control.shape[0]-1, loc = df_control.contact_views_number.mean(), scale = scipy.stats.sem(df_control.contact_views_number)))
# Building the interval for the df_test
print(scipy.stats.t.interval(0.95, df_test.shape[0]-1, loc = df_test.contact_views_number.mean(), scale = scipy.stats.sem(df_test.contact_views_number)))


#(0.6749539517949872, 0.6971436784914415)
#(0.6871939697365728, 0.7093031700924963)


## Mann Whitney test
# Use scipy.stats.mannwhitneyu(control_group_data, test_group_data, alternative = 'greater').
# Perform statistical analysis with the statistical criterion
print(scipy.stats.mannwhitneyu(df_control.contact_views_number, df_test.contact_views_number, alternative = 'greater'))
## MannwhitneyuResult(statistic=10745051401.0, pvalue=0.9435372065354772)

## Output Review of Mann Whitney Test on Non-Normal Indepdent Groups
# =============================================================================
# We have received the p-value that equals 0.94.
# 
# 0.94 > 0.05
# 
# Traditionally, if p ≤ 0.05, then there are enough arguments to reject the H0 and approve H1, although there is a small chance against this. 
# Then one can reject the H0 and say that the results are significant at the 5% level;
# 
# On the contrary, if p > 0.05, then there are not enough arguments to reject the H0. Without rejecting the H0, 
# we can state that the results are not significant at the 5% level.
# Our result means that we can not reject the H0 hypothesis.
# =============================================================================




## Upd Metric
# =============================================================================
# Do you recall we talked about the fact that we have to be careful while choosing metrics 
# for the A/B test? Let's try to add one metric to check if the result differs. 
# For example, we may try to find if the result changes if we use only users that have been 
# to the site earlier.
# =============================================================================
# Create the data that includes users that have visited the site for the first time
df = df.query('first_visit_after_test_start == 1')
# Control group
df_control = df.query('group == "control" ')
# Test group
df_test = df.query('group == "test" ')

# Perform statistical analysis with the statistical criterion
print(scipy.stats.mannwhitneyu(df_control.contact_views_number, df_test.contact_views_number, alternative = 'greater'))


## MannwhitneyuResult(statistic=2358361535.0, pvalue=0.14841766427319564)













