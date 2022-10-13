#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:54:06 2022

@author: craigrupp
"""

## Statistics
# =============================================================================
# Statistics is the science of collecting, organizing, interpreting, analyzing, and presenting numerical data. 
# Statistics methods are used in different areas: biology, medicine, physics, sociology, etc. Big samples of numerical data can be processed and described because of Statistics.
# 
# Collecting data: you are collecting all the data about some facts, events, etc. 
# For example, it can be the heights of each person in the specific group, the exchange course, amount of births and deaths yesterday – anything that can be represented as numerical data.
# 
# Organizing data: usually data is stored in tables, where each column is responsible for the single type. 
# For example, we got the table containing the student’s marks. Columns contain the final score for different subjects: History, Math, and Arts.

# Analyzing data: that's where we start to work with data and transform it into the facts. 
# Highlight the useful information, work with observations. Look if the result fits your goal.

# Interpreting data: now you have to explain your result. This is the process of translation from the numerical language to the human’s one. 
# The analyst should interpret the conclusion correctly.

# Presenting data: make your results viewable, use visualization tools. 
# It is much easier to perceive the plots and diagrams rather than just numbers.
# =============================================================================

# =============================================================================
# Data Types
# The analyst works mostly with numerical data: integer or floating. But this is not a comprehensive list.
# 
# Types of Data to Analyze
# Numerical: represented as a number.
# 
# integer
# floating

# Categorical: data that can be distributed into different classes or categories.
# 
# Nominal: each value belongs to the class, but order does not matter. For example, suggest that blood type can be one among the next: O, A, B, AB.
# Ordinal: like nominal, but now order matters. For example, there are four classes for people's age category: child, teen, adult, and retirement. The order is defined: a teen is younger than an adult but older than a child.
# =============================================================================


### Calculating Mean w/Python
# Declaring list in Python
marks = [10, 7, 9, 2, 10]
# sum() is used to add all element of list  
sum_of_marks = sum(marks)  
# len() function is used to find size of list
number_of_subjects = len(marks)
# Finding average of list  
average = sum_of_marks / number_of_subjects  
# Showing output
print("Average = ", average)

### Calculating Mean w/Numpy
import numpy as np
# Declaring numpy array
marks = np.array([10, 7, 9, 2, 10])  
# use mean() function 
average = marks.mean() 
print("Average = ", average)

temps = np.array([20, 22.5, 23.2, 19.4, 18.8, 21])
# arithmetic mean
a_mean = np.sum(temps) / len(temps)

print('Arithmetic mean:', a_mean)



### Geometric Mean
# =============================================================================
# Geometric Mean is usually used to evaluate not the sum of elements, but their product. 
# It helps to predict the average growth of some value.
# 
# For example, we have info on how the salary grows: 15% after the 1 year, 25% after 2 yrs, and 45% after the 3 yrs. 
# The average growth of salary during the 3 years is calculated like:
# 
# (1.15 * 1.25 * 1.45)^(1/3) = 1.277   (Equation : mu/mean = (a1 * a2* ...*an) ^ 1/n)
# 
# so the result is about 27.7% per year.
# =============================================================================

### Harmonic Mean
# =============================================================================
# Harmonic Mean is used to evaluate the average power, speed, or efficiency. Arithmetic Mean is often mistakenly used instead of the Harmonic. 
# We'll consider an example to calculate the average snail's velocity. It is known that a snail moved 10 meters with the 3 m/h velocity, and then 10 more meters with the 6 m/h velocity. 
# What's the average velocity?
# 
# The first thought is that it is equal to the Arithmetic Mean of velocities which is equal to 4.5 m/h. But we'll find it totally wrong after the calculations:
#     
# time1 = 10 meters / 3 = 3.333 hours
# time2 = 10 meters / 6 = 1.666 hours
# average velocity = (10 + 10)/(3.333 + 1.666) = 20 / (10/3 + 10/6) = 4 m/ h     
# velocity = 2/(1/3 + 1/6) = 4     (Equation : mu/mean = n / 1/a1 + 1/a2 + .... )
# =============================================================================
prices = np.array([100, 110, 114, 118, 119, 121, 127, 141, 178])
print(len(prices), prices.size)
# arithmetic mean
a_mean = np.sum(prices) / prices.size
# array length
n = prices.size
# geometric mean
g_mean = np.prod(prices) ** (1/n)
# harmonic mean
# To find the reverse elements of the list prices, write 1/prices.
print(1/prices)
h_mean = n / np.sum(1/prices)

print('Arithmetic mean:', a_mean)
print('Geometric mean:', g_mean)
print('Harmonic mean:', h_mean)

## Arithmetic >= Geometric >= Harmonic





## Median & Mode (Numpy)
# The Median is used in Statistics a lot. This is a middle value in the sorted set of the numbers:    
# =============================================================================
# This is a middle value in the sorted set of the numbers:
# 
# [1, 3, 4, 4, 4, 5, 7, 10, 15] : median is middle 4 
# [0, 3, 4, 5, 5, 10] : For the even number of elements, the median is the mean of two middle elements: (4+5)/2 = 4.5
# [40, 44, 56, 58, 64, 69, 70, 78] : (58 & 64 two middle numbers = 61)
# 
# Mode - Can be more than 1
# [16,18,18,17,19,17] : 17 & 18
# [45, 70, 90, 50, 65] : mode method would return : ModeResult(mode=array([45]), count=array([1])) : it returns the smallest mode and the number of its occureneces in the list.
# =============================================================================
from scipy import stats

prices = [400, 240, 310, 570, 990, 1000, 400, 990]
mode = stats.mode(prices)
median = np.median(prices)
print("Median = ", median)
print('Mode = ', mode)
print(type(mode))
print(mode[0], mode[1])
mode_num, mode_count = mode[0], mode[1]
print(mode_num, mode_count, type(mode_num), mode_num[0])
#[400] [2] <class 'numpy.ndarray'>

test_mult_modes = [5, 5, 5, 7, 7, 7]
print(stats.mode(test_mult_modes))
# ModeResult(mode=array([5]), count=array([3])) Returns lowest




## Variance 
# =============================================================================
# The variance is the Statistics measure to describe the spread between the values in the dataset. 
# In other words, the more the numbers differ from the mean, the greater the variance.
# 
# σ2 = ∑ (xi – x̄)2/(n – 1)
# x̄ is the mean/mu of data set.
# 
# ∑ (xi – x̄)2 is the sum of squares of difference of each observation from mean,
# 
# n is the total number of observations.
# =============================================================================
import statistics as stats
var_set = [7, 11, 15, 19, 24]
var_set_mu = sum(var_set) / len(var_set)
print(var_set_mu)
# 15.2
# Sum of squares of difference from mean
square_diffs = [(x - var_set_mu) ** 2 for x in var_set]
print(square_diffs)
# Som of squares divided by total observations - 1 (Sample Data)
print(f"Variance is {sum(square_diffs) / (len(var_set) - 1)}")
# Variance is 44.2
# https://www.geeksforgeeks.org/how-to-calculate-variance/

# Sum of squared divided by total observations (Population Data)
print(f"Variance is {sum(square_diffs) / (len(var_set))}")
# print(f"Variance is {sum(square_diffs) / (len(var_set))}")
# Variance is 35.36

# Numpy default is ddof=0 estiamte for normally distributed variables 
print(f"Variance for numpy is {np.var(var_set)}")
# Variance for numpy is 35.36

## Use numpy .var
stats.variance(var_set)
# 44.2


ages = [12, 20, 19, 23, 27, 18, 14, 28, 22, 16]
variance = np.var(ages)
# display results
print("Variance = ", variance)
# https://stackoverflow.com/questions/41204400/what-is-the-difference-between-numpy-var-and-statistics-variance-in-python
print(f"Variance with numpy and ddof 1 : {np.var(ages, ddof=1)}")
# Variance with numpy and ddof 1 : 27.43333333333333
print(f"Variance with stats library = {stats.variance(ages)}")
# Variance with stats library = 27.433333333333334

# =============================================================================
# In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of a hypothetical infinite population. 
# ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables.
# =============================================================================


# Anoter Example

numbers = [110, 120, 114, 150, 119, 199, 143, 182]
# use formula
# 1. find the mean value
mean = sum(numbers) / len(numbers)
# 2. iterate the array and find the sum of squared differences
total = 0 # total sum of differences
for num in numbers:
  total += (num - mean) ** 2

# 3. divide the sum and write to the var1
var1 = total / len(numbers)
print('Variance with formula = ', var1)
# Variance with formula =  966.859375

# calculate using numpy 
var2 = np.var(numbers)
print('Variance with numpy = ', var2)
# Variance with numpy =  966.859375

var1 == var2
# True



## Standard Deviation
# =============================================================================
# Like the variance, there is another concept to describe the spread called Standard Deviation. It is calculated as the square root from the variance.
# 
# The Standard Deviation gives similar info: the spread of data in the dataset. 
# The advantage of using Standard Deviation instead of Variance is that the first one describes the general range of numbers in the given dataset
# =============================================================================



pages = np.array([10, 15, 20, 18, 12])
std = pages.std()
print('Standard Deviation =', std)
# Standard Deviation = 3.687817782917155



pages = [10, 15, 20, 18, 12] # NOTE: no numpy array
std = np.std(pages)
print('Standard Deviation =', std)
# Standard Deviation = 3.687817782917155

summer_temps = np.array([20, 23, 26, 22, 27, 28, 30, 23, 21, 25])
year_temps = np.array([20, 27, 16, 12, 6, -2, -10, 3, 11, 15])

summer_std = summer_temps.std()
year_std = year_temps.std()
print('Std in the Summer', summer_std)
print('Std in Any Season', year_std)

# Std in the Summer 3.0740852297878796
# Std in Any Season 10.31309846748299





## Use Each with a data set
import pandas as pd
# importing data to dataframe
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/titanic.csv')
print(df['Age'].value_counts()) # Lots of counts in the 20s for ages 
# =============================================================================
# 24.00    30
# 22.00    27
# 18.00    26
# 19.00    25
# 28.00    25
# =============================================================================
print(df['Age'].isna().sum())
# 177 ... looks like a lot of nulls
data = df['Age'].dropna()
print(data.isna().sum())
# 0

info = {}
info['mean'] = data.mean()
info['mode'] = stats.mode(data)
info['median'] = np.median(data)

info['var'] = np.var(data)
info['std'] = np.std(data)
#print the values
print(info)
print(stats.mode(data))
# {'mean': 29.69911764705882, 'mode': 24.0, 'median': 28.0, 'var': 210.7235797536662, 'std': 14.516321150817317}


## Estimators' Robustness
# =============================================================================
# Robust Statistics are resistant to messed data, primarily to outliers - non-typically big or small values. 
# It means that values out of range do not affect the Statistics, so it is still a good estimator.
# =============================================================================
# =============================================================================
# Robust Values
# Median: since this is the middle value in the sorted dataset, the first and last values which are usually outliers do not affect.

# Non-Robust Estimators
# Arithmetic Mean: since it depends on the sum of all elements, the critical values may change the Mean value significantly.
# Variance: this metrics is actually the sum of squares, so huge values will affect it even more than the Arithmetic Mean value.
# Standard Deviation: since it is a square root out of Variance.


# The Mode can be or not be robust for different datasets and Data Distributions.
# =============================================================================

## Generate and mutate distribution of data

# generate the dataset of size 1000
np.random.seed(19)
data = np.random.normal(2, 12, 1000)
# calculate the values for dataset without outliers
mean = data.mean()
var = np.var(data)
median = np.median(data)
print(mean, var, median)

# add some huge outliers to the dataset
data = np.append(data, [100]*5)

# calculate new values
mean = data.mean()
var = np.var(data)
median = np.median(data)
print(mean, var, median)


print(np.median([5, 3, 9, 9, 11, 1, 12, 8, 1]))











