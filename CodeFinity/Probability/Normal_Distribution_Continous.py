#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:13:02 2022

@author: craigrupp
"""

## Continous Distributions 

### (Normal Distribution) - Most popular

# =============================================================================
# Continuous distribution is a distribution that has an infinite number of possible outcomes. 
# Therefore, we can not calculate the interval value or create a table because we do not know their amount. 
# Such distributions can be expressed only with a graph.
# 
# Let's start with the most widely used and gripping one, normal distribution!
# =============================================================================

## Norm Object Methods
# =============================================================================
# Let's recall some functions, bit for normal distribution (they are a little bit different):
# 
# For outputting random sample: norm.rvs(loc, scale, size).
# 
# For calculating the probability of receiving exactly x events: norm.pdf(x, loc, scale).
# 
# For calculating the probability of receiving x or more events: norm.sf(x, loc, scale).
# 
# For calculating the probability of receiving x or less events: norm.cdf(x, loc, scale).
# 
# loc is the mean value of the distribution.
# scale is the standard deviation value of the distribution.
# size is the number of samples of the distribution.
# x is the number of expected results.
# =============================================================================

# Confidence Intervals (Sample)
# =============================================================================
# Confidence interval: (Percent at which we estimate the distribution falling in between that interval)
# 
# In our exmaple with a mean of 1.2 and a standard deviation of 0.3 we can say that: 68.3% confidence we can say that the average imperial penguin's heigh is between 1.2 - 0.3 meters and 1.2 + 0.3 meters -> 0.9 and 1.5 meters. 
# 95.4% confidence we can say that the average imperial penguin's heigh is between 1.2 - 2 * 0.3 meters and 1.2 + 2 * 0.3 meters -> 0.6 and 1.8 meters. 
# 99.7% confidence we can say that the average imperial penguin's heigh is between 1.2 - 3 * 0.3 meters and 1.2 + 3 * 0.3 meters -> 0.3 and 2.1 meters.
# =============================================================================


## Dataset to play with
import pandas as pd
df_peng = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins.csv')
print(df_peng.head())
print(df_peng.columns)
print(df_peng.describe())

## We can use bill_length to create a distribution
bill_length = df_peng['bill_length_mm']
print(bill_length.value_counts())
# Any nulls?
print(bill_length.isna().sum())
# 2 found so let's just drop
bill_length = bill_length.dropna()
# Any nulls? (Double Check)
print(bill_length.isna().sum())
## Items to pass to rvs function for pandas series holding mean, std, count
print(bill_length.mean(), bill_length.std(), bill_length.count())


## Plotting/Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# distribution using series
sns.histplot(bill_length)
plt.show()

# distribution using pandas dataframe (with 2 missing values)
sns.histplot(data=df_peng, x='bill_length_mm')
plt.show()


## Create Random Distribution Sample with loc (aka mean) & scale (aka std) & can use count of column
## Count is ignoring null count
print(df_peng['bill_length_mm'].count(), df_peng.shape[0], len(df_peng)) 
from scipy.stats import norm

## Create Random Normal Distribution
sample_dist_png_bill = norm.rvs(loc=bill_length.mean(), scale=bill_length.std(), size=bill_length.count())

## Visualize Sample Distribution
sns.histplot(sample_dist_png_bill)
plt.show()


## Notice How Distribution follows bell type curve for the sample against the observed distribution which doesn't have as clean a distribution





## Task
# =============================================================================
# Here build the random distribution of the cat's weights! Follow the algorithm:
# 
# Import norm object from scipy.stats.
# Import matplotlib.pyplot with plt alias.
# Import seaborn with sns alias.
# Generate random normal distribution with the attributes:
# Mean equals 4.2.
# Standard deviation equals 1.
# Create a histplot with such parameters:
# dist variable to the data attribute.
# True variable to the kde attribute.
# Output the graph.
# =============================================================================

# Create random distribution
dist = norm.rvs(loc = 4.2, scale = 1, size = 1000) 
# Create a histogram
sns.histplot(data = dist, kde=True)

plt.xlabel("Weights")
plt.ylabel("Probability Density")
plt.title("Cat's Weights")
# Output the histogram
plt.show()









## Functions Usage/Challenges
# =============================================================================
# Please calculate the probability that your cat's weight will be exactly 5 kg. 
# Compare it to the graph and the values of confidence intervals. Assume that for this distribution, we have such parameters:
# 
# Mean equals 4.2.
# Stadard deviation equals 1.
# =============================================================================

# Calculate the probability
prob = norm.pdf(x=5, loc=4.2, scale=1)

print("The probability is", prob)


# Please calculate the probability that your cat's weight will be unusual!
# =============================================================================
# Calculate the first one prob_1 that the weight of your cat will be more than 11 kg with the parameters:
# Mean equals 4.2
# Standard deviation equals 1.

# Calculate the second one prob_2 that your cat's weight will be less than 2 kg with such parameters:
# Mean equals 4.2
# Standard deviation equals 1.

# Calculate the probability that the weight of your cat will be more than 11 or less than 2 kg.
# Compare it to the graph and the values of confidence intervals.
# =============================================================================

# Calculate the first probability
prob_1 = norm.sf(x = 11, loc = 4.2, scale = 1)
# Calculate the second probability
prob_2 = norm.cdf(x = 2, loc = 4.2, scale = 1)
# Calculate the whole probability
prob = prob_1 + prob_2

print("The probability is", prob)
