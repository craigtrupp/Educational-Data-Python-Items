#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:59:34 2022

@author: craigrupp
"""

## Variance
# =============================================================================
# Sometimes we will deal with several samples, and in this case, it is vital to figure out if there is any relationship between two samples.
# 
# We will start with discovering two independent samples; let's assume that they are distributed normally, and we know that we are working with the sample, not the whole population.
# Our task is to figure out if the sample means values are equal or not to conclude the sample's difference.
# 
# Firstly we should create the null hypothesis stating that two different mean values are equal. 
# But if we reject this hypothesis, we move to the second one that says that our mean values are different and, consequently, the samples do not belong to one population.
# 
# Null Hypothesis : H(0) - Two different means values are equal (μ1 = μ2)
# Alternative : H(1) - Two Samples' mean are different (μ1 != μ2)
# =============================================================================
# =============================================================================
# Student's T-test : Small Dist
# sem :  standard error of the mean 
# T = μ1 - μ2 / sem
# =============================================================================


## T-Test Conditions
# Samples are distributed normally.
# Homogeneity of variance : It is when we assume the equality or similarity of variances of two samples. (Levene Test - PValue Hello!)

## Levene's test (P-Value) (method that you will use not only in the case with normal distribution; it is universal and fits the situation when the distribution is not normal or has outliers!)
# =============================================================================
# If it is a test, we should state the null hypothesis. To do it, firstly, figure out the p-value. 
# There is nothing complicated here; it is just a value that we use to reject or not the null hypothesis; usually, the p-value equals 0.05. 
# But in the test, we will receive another p-value, let's call it a p-test. 
# If p-test < 0.05 (p-test < p-value), we reject the null hypothesis and reject the hypothesis that variances of two samples are equal; otherwise, we accept it, and variances are equal. 
# =============================================================================

## Task
# =============================================================================
# Assume that recently you've created two apps and want to know if they are equally successful. 
# You have two samples about the mean amount of users that download an app every day for one month.
# 
# sample_1 describes the first app with 87 observations, a mean value of 35, and a standard deviation of 2.78.
# sample_2 represents the second app with 79 observations, a mean value of 39.1, and a standard deviation of 2.99.
# Your task here is to check for the homogeneity of variances
# =============================================================================
# Import levene object
from scipy.stats import levene
# Import norm object
from scipy.stats import norm
import numpy as np

np.random.seed(0)

sample_1 = norm.rvs(size = 87, loc = 35, scale = 2.78)
sample_2 = norm.rvs(size = 79, loc = 39.1, scale = 2.99)

# Define the p-value
p_value = 0.05
# Conduct the Levene`s test
stat, p_test = levene(sample_1, sample_2)

print("Our p-value is", p_test)
# Check if we need to reject the null hypothesis
if p_test <  p_value:
    print("The variances of two samples are different")
else:
    print("The variances of two samples are equal")

# Our p-value is 0.462614712112142
# The variances of two samples are equal




## Equal Variance :  (Test Conditions Met with Homogeneity of variance above and sample being known to be distributed normally)
# =============================================================================
# The variances of two samples are equal this phrase is the result from the previous chapter! It means that the variances of the two samples are very similar, 
# and the samples do not vary from each other at all. So, if the variance is equal and the samples are distributed normally, we can conduct the test because 
# all requirements were met!
# =============================================================================
# =============================================================================
# ## Pooled Variance
# # If we know that the variances are equal, we can estimate the correlation between pooled data set (two samples) and the average of samples to conclude if they are identical.
# ## Equation
# # Pooled Variance = (sample1_var * deg_freedmom_sample1) + (sample2  * deg_freedmom_sample2) / deg_freedmom_sample1  + deg_freedmom_sample2
# =============================================================================

# =============================================================================
# ## Standard error : is a mathematical tool used in statistics to measure variability. 
# # It enables one to arrive at an estimation of what the standard deviation of a given sample is. 
# # It is commonly known by its abbreviated form – SE. Standard error is used to estimate the efficiency, accuracy, and consistency of a sample
# ## Equation : se = np.sqrt(pooled_var * (1 / len_1 + 1 / len_2))
# =============================================================================


len_1 = len(sample_1)
# Calculate the length of the second sample
len_2 = len(sample_2)

# Calculate the degrees of freedom for the first sample
df_1 = len_1 - 1
# Calculate the degrees of freedom for the second sample
df_2 = len_2 - 1

# Calculate the mean for the first sample
sample_1_mean = np.mean(sample_1)
# Calculate the mean for the second sample
sample_2_mean = np.mean(sample_2)

# Calculate the variance for the first sample
sample_1_var = np.var(sample_1)
# Calculate the variance for the second sample
sample_2_var = np.var(sample_2)

# Calculate the pooled variance using two samples who passed test
pooled_var = (sample_1_var * df_1 ) + (sample_2_var * df_2) / (df_1 + df_2)
# Calculate the standard error
se = np.sqrt(pooled_var * (1 / len_1 + 1 / len_2))

print("The mean of the first sample is", sample_1_mean)
print("The mean of the second sample is", sample_2_mean)
print("The variance of the first sample is", sample_1_var)
print("The variance of the second sample is", sample_2_var)
print("The pooled variance is", pooled_var)
print("The standard error is", se)

# The mean of the first sample is 35.02507220040284
# The mean of the second sample is 39.776864153766326
# The variance of the first sample is 8.260950582885165
# The variance of the second sample is 8.726647059072187
# The pooled variance is 714.5922286074391
# The standard error is 4.154416327872356



## Two-Tailed T-Test
# =============================================================================
# It is the test that helps us define if there is any difference in samples(increasing or decreasing in values). 
# Another wording allows us to determine if samples are equal or not.
# 
# (With Significance Level at 0.05)
# We should divide the significance level by two because it is a two-tailed test, and if our value falls into 2.5% data from the right, 
# it means that the mean of the first sample is greater than the second; otherwise, if our value falls into 2.5% data from the left, 
# it means that the mean of the first sample is less than the second. If, in general, we claim that a = 0.5, the confidence level will be 1 - a/2 = 0.975.
# =============================================================================
## Conduct T-Test
# =============================================================================
# 1. Find the value of t-students statistics (value of t), but it is better to use a module of the differences of the mean values, let it be t variable.
#     t = μ1 - μ2 / SE (Standard Error)
# 2. Find the critical value for the two-tailed test, 
#     t-critical: t_critical = stats.t.ppf(q=0.975, df=df) 
# here we conduct a test with the a value equal to 0.05, and put a sum of degrees of freedom of the explored samples.
# 3. Find the new p-value to which we will compare p-critical in our t-test :  
#         p_value_two_tailed = 2*(1 - stats.t.cdf(x = t, df = df))
# as the first argument, we put the value of t-statistics, and as the second one, we put the sum of degrees of freedom for two samples.
# 4. Check if the p_value_two_tailed is more significant than a value of 0.05. We support the null hypothesis if this condition is proper; otherwise, we reject it.
# =============================================================================
# bring in stats library
import scipy.stats as st
# Calculate t value
t = abs(sample_1_mean - sample_2_mean) / se
# Calculate critical value : a level 0.05
t_critical = st.t.ppf(q = 0.975, df = df_1 + df_2)
# Calculate p-value
p_value_two_tailed = 2 * (1 - st.t.cdf(x = t, df = df_1 + df_2))
# Check the null hypothesis
if p_value_two_tailed > 0.05:
    print("We support the null hypothesis, the mean values are equal")
# Check the alternative hypothesis
else:
    print("We reject the null hypothesis, the mean values are different")
print("t-statistics value equal to", t)
print("t-critical value equal to", t_critical)

# We reject the null hypothesis, the mean values are different
# t-statistics value equal to 10.498231324238853
# t-critical value equal to 1.974534575852265


## Python Conduct Sample T-Test
# =============================================================================
# Python formula for the sample t-test
# 
# st.ttest_ind(a = sample_1, b = sample_2, equal_var=True), it returns two values: the first one is t-statistics and the second one is the p-value. 
# The arguments are pretty simple; the first and second corresponding to the discovered samples, and the third define homogeneity of variance.
# =============================================================================


## Task
# As we check the homogeneity of variance and know that the samples are normally distributed, we can boldly apply the t-test to our samples.


# Apply t-test
stats, p_test = st.ttest_ind(a = sample_1,
                          b = sample_2,
                          equal_var = True)

# Check if we should support or nit the null hypothesis
if p_test > 0.05:
    print("We support the null hypothesis, the mean values are equal")
else:
    print("We reject the null hypothesis, the mean values are different")

# We reject the null hypothesis, the mean values are different




## Paired T-Test
# =============================================================================
# You finished the first test and figured out that the mean value of users that download the app is different! 
# So, now it is time to dive into a fascinating test that looks almost the same but is just a little bit complicated.
# =============================================================================

# Scenario
# =============================================================================
# Let's assume that you have a successful app and want to figure out if the number of users that download the app will statistically increase 
# during one month if you change the logo. We should have statistical proof that the mean value has decreased; we can not just compare two mean values and conclude. 
# So, you have two samples: one before changes and another after. Such samples are called dependent and require paired t-test.
# =============================================================================

# Conditions for Test
# =============================================================================
# Samples should be normally distributed.
# Samples should not contain outliers.
# Samples should have equal lengths.
# =============================================================================

# Conduct - stats.ttest_rel(sample_a, sample_b)
# =============================================================================
# st.ttest_rel(a, b) is similar to the function for independent samples, but here we do not obligate to check the homogeneity of variance; 
# we just put two samples that should be discovered. In the output, you will receive two values the first one is t-statistics and the second one is the p-value. 
# The condition for supporting or rejecting the null hypothesis is the same for all tests.
# =============================================================================
np.random.seed(0)

sample_1_paired = norm.rvs(size = 104, loc = 91, scale = 2.78)
sample_2_paired = norm.rvs(size = 104, loc = 92, scale = 2.78)

# Conduct paired t-test
stats, p_test = st.ttest_rel(sample_1_paired, sample_2_paired)

# Check the null hypothesis
if p_test > 0.05:
    print("We support the null hypothesis, the mean values are equal")
# Check the alternative hypothesis    
else:
    print("We reject the null hypothesis, the mean values are different")
    
    
    



## Mann-Whitney U test
# =============================================================================
# We have already learned how to conduct the t-test, and we have recognized that this test requires a lot! 
# Our samples should be normally distributed, and the variances should be equal... But what should we do if we want to compare two independent samples but do not want to change them?
# =============================================================================

## Scenario (See Image in Ghub Repo for Assocation - Ranging Concept - Big to Small for each sample (high to low or vice versa (doesn't matter)) then count sum of ranged values for each group)
# =============================================================================
# The main principle is to divide your data into groups and range it. Look at the picture where we can observe houses from the first city(purple houses) and houses from the second city(yellow houses), and they vary because of their size:
# 
# 1) In the first part of the picture, you can see six different houses of different sizes.
# 2) In the second part of the picture, we ranged all houses; the first one (the biggest) has the range 1, the second one (smaller than the biggest one) has the range 2 and the smallest one here has the range 6.
# 3) Then we divide our houses by cities and count the sum of ranges, and if the sum of ranges for different cities varies significantly, we can assume that the sizes of houses vary too and vice versa.
# =============================================================================

## Next Step - U-test
# =============================================================================
# The first step in conducting a u-test is to determine if the shape of distributions is equal; 
# they have equal amounts of peaks and approximately similar types. If they are equal, you should compare medians of two samples; otherwise, mean values.
# =============================================================================


## Task
# =============================================================================
# We will discover the prices of cars Ford Focus and Ford Fiesta; our task is to determine if the mean prices of the two models are equal. 
# If not, we will discover which model is more expensive. 
# Firstly let's compare the distributions' shapes
# =============================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read csv file about Ford Fiesta
data_fiesta = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/Fiesta')
# Read csv file about Ford Focus
data_focus = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/Focus')

# Build a histplot for Ford Fiesta
sns.histplot(data = data_fiesta,
            x = 'price',
            color = 'b',
            kde = True,
            label = 'Fiesta')
# Build a histplot for Ford Focus
sns.histplot(data = data_focus,
            x = 'price',
            color = 'y',
            kde = True,
            label = 'Focus')

plt.legend()
plt.show()


## Task Cont : Check If the Data Has Outliers - Box Plots!
# =============================================================================
# As you may recognize, the shapes of our data are not equal; one distribution even has two peaks, so the right way here is to compare mean values.
# 
# The next step in our test is not obligatory; we should be sure that u-test is appropriate here, so as you remember, this test can deal with samples with outliers. 
# The best way to check them is to create boxplots! So, your task in this chapter is just to ascertain that our data are not so beautiful
# =============================================================================
# Create DataFrame
price = pd.DataFrame({'Focus': data_focus['price'], 'Fiesta' : data_fiesta['price']})
print(price.tail())
print(price['Focus'].isna().sum())
print(price['Fiesta'].isna().sum())


# Build a boxplot using Dataframe with dataset price columns
price.boxplot(column=['Focus', 'Fiesta'])
plt.ylabel('Price')
plt.show()


## Task Cont : Compare Mean - st.mannwhitneyu
# =============================================================================
# We've prooved our data full of outliers, so we can conduct U-test for the prices of Ford cars.
# 
# As usual, let's figure out the hypothesis:
# 
# The null hypothesis: the mean prices for two cars are equal;
# The alternative hypothesis: are the mean prices for the two cars vary.
# The condition for supporting the null hypothesis is the same: if the p-value received in the test is greater than the defined p-value(0.05), 
# we support the null hypothesis; otherwise, we reject it.
# 
# Function for calculating U-test: 
# statics, p_value = st.mannwhitneyu(x = sample_1, y = sample_2, alternative = 'two-sided')
# 
# x = sample_1 the first sample,
# y = sample_2 the second sample,
# alternative = 'two-sided' means that we are providing a two-tailed test here to figure out are the means different (now, it is no matter if one mean is bigger than another).
# As a result, we will receive the u-statistics variable the p_value, which should be compared. 
# =============================================================================
# Conduct U-test
statics, p_value = st.mannwhitneyu(x = data_focus['price'],
                         y = data_fiesta['price'],
                         alternative = 'two-sided')
# Print the results
print(statics, p_value)

# Check the null hypothesis
if p_value > 0.05:
    print("We support the null hypothesis, the mean values are equal")
else:
    print("We reject the null hypothesis, the mean values are different")

# 21463134.5 0.0
# We reject the null hypothesis, the mean values are different
    




## Deal with One-Tailed Test - Which of Two samples has a greater mean value
# =============================================================================
# We know that mean values are different, but it is time to check which model, on average, is more expensive.
# 
# It is time for you to dive deeper into the one-tailed test. It differs from the two-tailed test because this one helps 
# us find out which of the two samples has a greater mean value
# =============================================================================
## What is the one-tailed test?
# =============================================================================
# Imagine that we have two samples and, consequently, two hypotheses.
# 
# # First Case
# The null hypothesis: the first sample is greater than or equal to the second sample.
# The alternative hypothesis, the second sample is less than the first sample.
# 
# In the first picture, you can see the right one-tailed test that helps us figure out if the first sample is greater than the second; 
# it means that our data should fall to the left of the red line; otherwise, we reject the null hypothesis.
# 
# # In the second case, let's assume:
# 
# The null hypothesis: the first sample is less than the second sample.
# The alternative hypothesis, the second sample is greater than or equal to the first sample. 
# 
# In the second picture, you can see the left one-tailed test that helps us figure out if the first sample is less than the second, 
# which means that our data should fall to the right of the red line; otherwise, we reject the null hypothesis.
# =============================================================================
## Functions
# =============================================================================
# statics, p_value = st.mannwhitneyu(x = sample_1, y = sample_2, alternative = 'less') 
# - check if the sample_1 mean is less than the sample_2 mean.(alternative hypothesis: sample_1 is less)
# 
# statics, p_value = st.mannwhitneyu(x = sample_1, y = sample_2, alternative = 'greater') 
# - check if the sample_1 mean is greater thsn the sample_2 mean (alternative hypothesis: sample_1 is greater).
# =============================================================================

## Task
# =============================================================================
# Let's assume the hypotheses:
# 
# The null hypothesis: the Ford Fiesta model cheaper than the Ford Focus model.
# The alternative hypothesis: the Ford Fiesta model more expensive or equal to the Ford Focus model.
# Follow the algorithm to reject one of them:
# =============================================================================
# Conduct U-test
statics, p_value = st.mannwhitneyu(x = data_fiesta['price'],
                      y = data_focus['price'],
                      alternative = 'greater')
print(statics, p_value)

# Check the hypothesis
if p_value > 0.05:
    print("We support the null hypothesis, the mean price of Ford Fiesta is less than the Ford Focus")
else:
    print("We reject the null hypothesis, the mean price of Ford Fiesta is greater than or equal to the Ford Focus")

## 8620381.5 1.0
## We support the null hypothesis, the mean price of Ford Fiesta is less than the Ford Focus





## Another Hypotheses
# =============================================================================
# Let's assume another hypotheses, to test out u-test in Python:
# 
# The null hypothesis: the Ford Fiesta model more expensive than or equal to the Ford Focus model.
# The alternative hypothesis: the Ford Fiesta model less expensive than the Ford Focus model.
# Follow the algorithm to reject one of them:
# =============================================================================

data_fiesta = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/Fiesta')
data_focus = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/Focus')

# Conduct U-test
statics, p_value = st.mannwhitneyu(x = data_fiesta['price'],
                                 y = data_focus['price'],
                                 alternative = 'less')
print(statics, p_value)

# Check the hypothesis
if p_value > 0.05:
    print("We support the null hypothesis, the mean price of Ford Fiesta is greater than or equal to the Ford Focus")
else:
    print("We reject the null hypothesis, the mean price of Ford Fiesta is less than the Ford Focus")

# Check the mean values
print(np.mean(data_fiesta['price']), np.mean(data_focus['price']))


# =============================================================================
# 8620381.5 0.0
# We reject the null hypothesis, the mean price of Ford Fiesta is less than the Ford Focus
# 10196.298002135123 13185.88295553618
# =============================================================================



## Seems The Null Hypothesis is essentially just the inverse of our alternative argument based on the positioning of our two samples
# =============================================================================
# first hypotheses (lines 415 - 417) : Null Hypothesis confirmed for fiesta price being less w/alternative set to greater 
# second hypothes (lines 446 - 448) : Null Hypothesis rejected for fiesta being greater or equal to ford focus w/alternative set to less
# =============================================================================















