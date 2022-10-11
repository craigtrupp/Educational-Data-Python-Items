#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:07:14 2022

@author: craigrupp
"""

# Discrete Distributions


# Theory & Discrete Distribution Defined
# =============================================================================
# Discrete distribution is a distribution that has a finite number of possible outcomes.
#Some theory:

# Mean of the distribution, also called the expected value, defines the sample's average value. 
# Standard deviation expresses how much the random value from the sample differs from the mean.
# =============================================================================


# Uniform Distribution
# =============================================================================
# Key characteristics:
# 
# Each outcome is equally likely to happen.
# 
# Example:
# 
# When we roll a dice, it is always an equal probability for each event. 
# As we remember from this chapter, the probability is a fraction where the amount of the desired outcome is the numerator and the amount of all outcomes is the denominator.

# There is no point in talking about mean and standard deviation here; the reason is that all outcomes are equally likely to happen. 
# There are no deviations or outliers. By the way, we even can not make a prediction based on uniform distribution
# =============================================================================

# Uniform Distribution Sample
# =============================================================================
# Create uniform distribution with the size 20000.
# Create the histplot from Seaborn based on uniform distribution.
# =============================================================================
# Import relevant libraries
import seaborn as sns
from scipy.stats import uniform
import matplotlib.pyplot as plt

# Create 'uniform' distribution
dist = uniform.rvs(size = 20000)

# Create the histplot
sns.histplot(data = dist)
plt.show()


## Further Uniform Distribution Sample(s) 
# =============================================================================
# Have you ever wonder that your friends birthday could be any day of the year with equal probability. 
# The probability for each day creates uniform distribution.
# =============================================================================
# =============================================================================
# Let's recall some functions, but for the uniform distribution (they are a little bit different): For calculating the probability of receiving exactly defined output x :
# 
# uniform.pdf(x, loc, scale).
#   For calculating the probability of receiving exactly defined output x :
# 
# uniform.sf(x, loc, scale)(inclusive).
#   For calculating the probability of receiving output that is bigger than x::
# 
# uniform.cdf(x, loc, scale)(inclusive).
#    For calculating the probability of receiving output that is less than x:
    
# loc is the lower bound of the distribution (minimum value).
# scale is the upper bound of the distribution (maximum value).
# =============================================================================

# Birthday is January 10th
print(uniform.pdf(12, 1, 365))
# Probability of uniform pdf function that each day is evenly weighted or a 
print(1/365)
print(f"There is a equal chance on any given day that someone's birthday is a : {round(uniform.pdf(12, 1, 365) * 100, 5)}% chance")

# =============================================================================
# Task
# 
# Imagine that you met a person and want to calculate the probability of his birthday in summer, you know he wasn't born on a leap year.

# Calculate the probability that he was born after the 152nd day of the year (the 1st of June). 

# Calculate the probability that he was born before the 243rd day of the year (the 31st of August). 

# Calculate the probability that he was born before the 243rd day of the year and after the 152nd day of the year. (Multiply Rule - First & Second Event)
# =============================================================================

## After 152nd day
aft_152 = uniform.sf(152, 1, 365)
print(aft_152)
print((365-152)/365) # Oh what ya know they're the same

## Before 243rd 
bfr_243 = uniform.cdf(243, 1, 365)
print(bfr_243)
print(243/365)

## Combined ( Birthday > 152 && Birthday < 243) - And Multiply Rule for Separate Probability Events
print(aft_152 * bfr_243)






## Bernoulli Distribution
# =============================================================================
# Key characteristics:
# 
# Only 1 trial.
# 
# Only 2 outcomes.

# Mean and standard deviation can also be calculated with Python, using this syntax bernoulli.mean(p), bernoulli.std(p), where p is the probability of success.
# =============================================================================
# =============================================================================
# Do you remember .pmf() function? In general, this function helps us to find the probability that the event will happen (if we know the probability of success). 
# Try to use it to define the probability of an event with Python; the syntax is bernoulli.pmf(k, p), where k is the event (0 or 1 in our case), and p is the probability of success.
# =============================================================================

# Task
# =============================================================================
# Calculate the probability to receive the event 1 with the probability of success 0.7.
# Calculate the distribution mean with the probability of success 0.7.
# Calculate the distribution standard deviation, with the probability of success 0.7.
# =============================================================================
from scipy.stats import bernoulli
# Check the probability for the event 1 and 0
print("The probability is", bernoulli.pmf(1, 0.7))
# Check the mean
print("The mean is", bernoulli.mean(0.7))
# Check the standard deviation
print("The standard deviation is", bernoulli.std(0.7))




## Binomial Distribution
# =============================================================================
# Key characteristics:
# 
# This distribution is the same as the Bernoulli distribution, which is repeated several times.
# Multiple Trials (Only 2 Outcomes Per Trial)
# 
# Example:
# 
# Tossing a coin is a Bernoulli distribution, but tossing one coin 3 times creates a binomial distribution.
# =============================================================================

# Task
# =============================================================================
# Imagine you passing a test that includes 12 questions; there are just two answers for each question (one of them is correct, another isn't correct).
# You have excellent marks, and you know that if you receive less than 6 or exactly 7 points, you will spoil it.

# Calculate the probability of receiving 6 or less points in the test where the probability of answering right is 0.5 and the number of questions is 12.
# Calculate the probability of receiving exactly 7 points in the test where the probability of answering right is 0.5 and the number of questions is 12.
# Calculate the whole probability.
# =============================================================================
from scipy.stats import binom
import numpy as np
np.random.seed(2000)

# Calculate the first probability
prob_1 = binom.cdf(k = 6, n = 12, p = 0.5)
# Calculate the second probability
prob_2 = binom.pmf(k = 7, n = 12, p = 0.5)
# Calculate the whole probability
prob = prob_1 + prob_2

# Print the probability
print("The probability is", prob)




## Challenge
# =============================================================================
# Task
# 
# Let's assume that we want to conduct an experiment to determine the probability that a person has more than 3 cats, 
# let's consider that we have asked 1000 people (they can answer yes or no). (Key here is the 2 available outcomes from survey)

# Calculate the probability that more than 200 people answered yes to your question among 1000 that were interviewed. 
# The probability of receiving a positive answer is 0.3 or 30%.
# =============================================================================
# Import binom object
import numpy as np
np.random.seed(2000)

# Calculate the probability
prob = binom.sf(k=200, n=1000, p=0.3)

# Print the probability
print("The probability is", prob)




## Poisson Distribution
# =============================================================================
# To work with this distribution, we should import the poisson object from scipy.stats, 
# and we you can apply numerous functions to this distribution like pmf, sf, and cdf that were already learned.
# =============================================================================
# =============================================================================
# Key characteristics:
# 
# It measures the frequency over a specific time interval.
# 
# Example:
# 
# The data on how often your application had a certain number of users during its entire existence.
# =============================================================================


# Sample Code For An Average of 50 users (mean 50) over 10,000 days (interval) - Return is a distribution showing count or total days/frequency for each bin around the mu/mean
# =============================================================================
# poisson.rvs(mu = 50, size = 10000):
# 
# mu means mean (here, it was defined randomly).
# size is the number inverted by the sum of all values ​​of the frequencies of the column
# =============================================================================

from scipy.stats import poisson
fig, ax = plt.subplots()
dist = poisson.rvs(mu = 50, size = 10000)
plt.xlabel("The Amount of User")
plt.ylabel("Frequency")
plt.title("Poisson Distribution")
ax.hist(dist, bins = 40)
plt.show()


## Let's recall some functions, but for Poisson distribution (they are a little bit different):
# =============================================================================
# For calculating the probability of receiving exactly k events: poisson.pmf(k, mu).
# 
# For calculating the probability of receiving k or more events: poisson.sf(k, mu).
# 
# For calculating the probability of receiving k or less events: poisson.cdf(k, mu).
# =============================================================================

# Task
# =============================================================================
# Calculate the probability that your site has more than 80 visitors with the mean value 50.
# Calculate the probability that your site has less than 20 visitors with the mean 50.
# Calculate the whole probability - the probability that your site has more than 80 or less than 20 visitors.
# This task is a real-life challenge due to the reason that you calculate the probability of coping with a small or large amount of users.
# =============================================================================
# Calculate the first probability
prob_1 = poisson.sf(k = 80, mu = 50)
# Calculate the second probability
prob_2 = poisson.cdf(k = 20, mu = 50)

# Calculate the whole probability
prob = prob_1 + prob_2

print("The probability is", prob)



## Another Example
# =============================================================================
# Imagine you posted something to your favorite social network and decided to calculate the number of likes and decide to calculate the probability receive 990990 likes. Follow the algorithm:
# 
# Import poisson object.
# Calculate the probability of receiving exactly 990990 likes with the mean value 1000000.
# =============================================================================
# Calculate the probability
prob = poisson.pmf(k = 990990, mu = 1000000)

print("The probability is", prob)




















