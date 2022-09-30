#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:23:46 2022

@author: craigrupp
"""

## Probability Theory First Section

# =============================================================================
# The random variable is a quantity that equals one and only one value depending on the result of testing result.
# 
# Let's assume that X is the random variable with several outcomes (getting head or tail); therefore, we can mark them as x1 and x2.
# Probability (P) = quantity of desired outcomes (n) / the quantity of all outcomes (m)
# =============================================================================
# Assign to the variable 'green' the amount of green balls
green = 10
# Assign to the variable 'all_balls' the amount of all balls
all_balls = 29

# Calculate the probability
probability = green/all_balls
print(probability)
## 0.3448275862068966
print(f"We can also commonly multiply by 100 for a percentage {round(100 * probability,2)}%")
## We can also commonly multiply by 100 for a percentage 34.48%


# Bernoulli trial
# =============================================================================
# We can calculate that the probability of tossing a coin once and getting a head is 50 %.
# Scientifically it is called : Bernoulli trial.
# 
# It is a random experiment with only two outcomes: failure or success. 
# Therefore, we can express an opinion that tossing a coin is a Bernoulli trial too.
# =============================================================================

## Input:
# Import relevant libraries 
from scipy.stats import bernoulli

# Here, you simulate an experiment of tossing 5 coins (and get different results as no seed for random has been defined)
experiment = bernoulli.rvs(p = 0.5, size = 5)
print(experiment)


## Code Detail
# =============================================================================
# 1. You need to import bernoulli object from scipy.stats. With this object, we will conduct a probability experiment on a computer.
# 2. bernoulli.rvs(p = 0.5, size = 5) means that the probability of getting head/outcome is 50 %, p = 0.5, the sample size in experiment is 5, size = 5.
# 3. The output shows an array with five results for each coin,  1 means success and 0 means failure.
# 4. For my output : [1 1 0 0 1], I received three positive results for a "heads" at the indexes with a 1 
# =============================================================================

# Update Experiment / Set np.random.seed() for uniform testing results
import numpy as np

# Setting the seed here will get a identical output should the seed be set at time of the execution with the variable 
np.random.seed(19)

experiment = bernoulli.rvs(p = 0.7, size = 10)
print(experiment)


# Binomial probability
# =============================================================================
# It is when we have a defined number of successful trials among all attempts 
# in an experiment with two outcomes.
# =============================================================================

# Import relevant library
from scipy.stats import binom
# Here, we simulate an experiment of tossing 5 coins three times
experiment = binom.rvs(p = 0.5, size = 5, n = 3)
print(experiment)
## [2 2 2 2 2]
## [1 2 0 1 2]

## Code Detail
# =============================================================================
# We need to import binom object from scipy.stats.
# binom.rvs(p = 0.5, size = 5, n = 3) means that the probability of getting head is 50 %, p = 0.5; 
# the size of sample in experiment is 5, size = 5; the number of trial is 3, n = 3.
# In the output we can see an array with five results for each coin with the number of successful trials for each coin.
# =============================================================================

# Set static return
np.random.seed(29)
five_coins = binom.rvs(p=0.5, size=5, n=5)
print(five_coins)

# =============================================================================
# np.random.seed(29)
# five_coins = binom.rvs(p=0.5, size=5, n=5)
# print(five_coins)
# [4 2 1 3 2]
# 
# five_coins = binom.rvs(p=0.5, size=5, n=5)
# print(five_coins)
# [3 3 4 3 3]
# =============================================================================
# =============================================================================
# five_coins = binom.rvs(p=0.5, size=5, n=5)
# print(five_coins)
# [2 3 1 2 3]
#
# np.random.seed(29)
# five_coins = binom.rvs(p=0.5, size=5, n=5)
# print(five_coins)
# [4 2 1 3 2]
# =============================================================================
