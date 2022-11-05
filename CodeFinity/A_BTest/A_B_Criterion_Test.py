#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:17:16 2022

@author: craigrupp
"""

# =============================================================================
# A/B Testing 
# =============================================================================
# =============================================================================
# To answer these questions, we have to perform an A/B test. 
# The first version of the site you have seen is called the control version (A). 
# The updated version is called the test version (B).
# =============================================================================

## Statistical Criterion
# =============================================================================
# A statistical criterion is a mathematical rule that allows us to reject the null hypothesis or not, 
# that is, to conclude whether there is a non-random difference between groups. 
# A statistical criterion creates a p-value.
# A statistical significance is a measure of confidence that a result is not random. 
# By default, a statistical significance of 5%(or 1%) is used.
# =============================================================================
# =============================================================================
# p-value > statistical significance - We can not decline the H0 (Null) hypothesis
# p-value < statistical significance - We can accept the H1 hypothesis & Reject Null 
# =============================================================================

## Picking Criterion

# Import pandas 
import pandas as pd 
# Import the seaborn
import seaborn as sns
# Import the scipy
import scipy.stats
# Import the statsmodels.api
import statsmodels.api as sm
# matplotlib
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/ae14b913-9d96-48cb-ace7-a332315f7cf4/ab+test+1.csv')

# Build the distplot
sns.distplot(df.clicks)
# Build the qqplot
sm.qqplot(df.clicks, line = 's')
# Perform the normaltest
print(scipy.stats.normaltest(df.clicks))
# NormaltestResult(statistic=4.878079675838946, pvalue=0.08724458019660701)

## Normal Distribution - normaltest
# =============================================================================
# From the previous chapter, we learned that if the normaltest shows the value > 0.05, 
# the distribution is normal.
# =============================================================================

## As we have a normal distribution, our criterion will be a t-criterion (Student's criterion).

## Control & Test Groups
# =============================================================================
# Let's divide our data into 2 groups:
# 
# The control group that tests the old version of the site;
# The test group that tests an updated version of the site.
# =============================================================================
print(df.columns.tolist())
print(df['group'].value_counts())

# Create the new variable df_control with the 'control' group
df_control = df.query('group == "control"')
print(df_control)
# Create the new variable df_test with the 'test' group
df_test = df.query('group == "test" ')
  
# Show the first row of the df_control
print(df_control.head(1))
# Show the first row of the df_test
print(df_test.head(1))


# Build the distpot for the df_control
sns.distplot(df_control.clicks, label='control')
# Build the distplot for the df_test
sns.distplot(df_test.clicks, label='test')
plt.legend()
plt.show()


## Create Confidence Intervals
# =============================================================================
# A confidence interval is the mean of your estimate plus and minus the variation 
# in that estimate. This is the range of values you expect your estimate to fall between 
# if you redo your test, within a certain level of confidence. Confidence, in statistics, 
# is another way to describe probability.

## To build them use scipy.stats.t.interval(alpha, data, loc, scale)
# In our case we will use alpha equals 0.95(you may also choose 0,99, but you will need to compare the p-value with 0,01 thus), 
# the data.shape[1] as a data, loc = data.clicks.mean() and scale = scipy.stats.sem(data.clicks).
# =============================================================================
print(df_control.shape, df_control.shape[1])
cf_control_95 = scipy.stats.t.interval(0.95, df_control.shape[1], loc=df_control['clicks'].mean(), scale=scipy.stats.sem(df_control['clicks']))
print(cf_control_95) # (36.3986254753268, 44.01516762812147)
cf_intv_test_95 = scipy.stats.t.interval(0.95, df_test.shape[1], loc = df_test.clicks.mean(), scale = scipy.stats.sem(df_test.clicks))
print(cf_intv_test_95) # (46.59049739608274, 53.40950260391726)



# T-Test
# =============================================================================
# So, we have studied how do 2 groups' distributions look like:
# 
# Their plots don't look similar;
# Their confidence intervals don' cover each other a lot.
# Earlier, we decided that we were going to use t-criterion criterion to cope with our problem. \
# It is our last check to prove whether there is a NON-RANDOM difference between groups.
# =============================================================================
print(scipy.stats.ttest_ind(df_control.clicks, df_test['clicks']))
## Ttest_indResult(statistic=-6.097212953016276, pvalue=1.0556744440878422e-07)


## Quick Summation
# =============================================================================
# We have received the p-value that equals the number that ≤ 0.05:
# 
# Traditionally, if p ≤ 0.05, then there are enough arguments to reject the H0 and approve H1, 
# although there is a small chance against this. Then one can reject the H0 and say that the 
# results are significant at the 5% level;
# 
# On the contrary, if p > 0.05, then there are not enough arguments to reject the H0. 
# Without rejecting the H0, we can state that the results are not significant at the 5% level.
# =============================================================================

























