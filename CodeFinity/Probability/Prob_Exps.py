#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:43:04 2022

@author: craigrupp
"""
### Binom.pmf
# =============================================================================
## Scenario
# Imagine that we are working for a real estate agency, and we need to know how many positive answers 
# we will get from all interviewees.
# 
## Experiment
# In this experiment, we will work with the binom.pmf(k, n, p) function. 
# This function helps calculate the probability of receiving exactly k successes among n trials 
# with the probability of success for each experiment p.
# =============================================================================

## Task
# =============================================================================
# Calculate the probability of getting 1000 positive answers about the flat purchase among 20 000 people.
# We know that the probability of having a positive response about buying real estate is 20%.
# =============================================================================
from scipy.stats import binom
# Calculate probability
tsk_prb = binom.pmf(k=1000, n=20000, p=0.2)
print(tsk_prb)
## 0.0

# Explanation
# =============================================================================
# binom.pmf(k = 1000, n = 20000, p=0.20) the probability of getting 1000 successes 
# amoung 20 000 trials with the probability of success 20%.
# The result of our code is zero, but we worked with an enormous sample; in the task, we will receive a more understandable result.
# =============================================================================

## Task - Take Note of Low Probability w/pmf As Exact Probability is Being Returned!
# =============================================================================
# Your task here is to calculate the probability that exactly 5 kittens will find a home; there are 12 kittens in the shelter. 
# In this city, kittens are taken from a shelter with a probability of 75%. 
# 
# Calculate the probability that exactly 5 kittens out of 12 will find a home with the probability of success 75%.
# =============================================================================
# Calculate the probability
experiment = binom.pmf(k = 5, n = 12, p = 0.75)
print("The probability is", experiment, f"a {round(100*experiment,3)}% chance of exactly 5 being adopted")
## The probability is 0.011471271514892587 a 1.147% chance of exactly 5 being adopted




## Second Experiment - Binom.sf (Threshold >= k)

# Note
# =============================================================================
# As we remember from the previous chapter, it was almost impossible to figure out the probability of 
# getting exactly 1000 positive responses among 20 000 answers, with the probability of 20% of getting a positive answer
# =============================================================================
## Alter
# =============================================================================
# Here, we should calculate the probability of getting 1000 or more positive answers.
# =============================================================================
## Binom.sf - Threshold
# =============================================================================
# In this experiment, we will work with the binom.sf(k, n, p) function. 
# This function helps calculate the probability of receiving k or more successes 
# among n trials with the probability of success for each experiment p.
# =============================================================================

## Above Scenario with binom for 1000 successes estimate
snd_exp_1k_more = binom.sf(k=1000, n=20000, p=0.2)
print(snd_exp_1k_more)
## 1.0    100% chance of at least 1000 happening with large sample size and 20% probability of event

## Cats Scenario (5 or more from same probability total number of kittens)
# =============================================================================
# Your task here is to calculate the probability that 5 or more kittens will find a home, 
# there are 12 kittens in the shelter. In this city, kittens are taken from a shelter with a probability of 75%.
# =============================================================================
cts_fve_more = binom.sf(k=5, n=12, p=0.75)
print(cts_fve_more, f"or {round(cts_fve_more*100,3)}% chance of at least 5 or more from the 12 being adopted")
## 0.985747218132019 or 98.575% chance of at least 5 or more from the 12 being adopted



## Third Experiment - binom.cdf (Threshold <= k)
# =============================================================================
# In this experiment, we will work with the binom.cdf(k, n, p) function. 
# This function helps calculate the probability of receiving k or less successes
# among n trials with the probability of success for each experiment p.
# =============================================================================

## Real Life Example
# =============================================================================
# Imagine that we are working for the bank, and last month the bank gained 200 customers; 
# we know that the probability for clients to continue working with the bank is 60%. 
# Calculate the probability that 70 or fewer customers will stay with
# =============================================================================
bnk_retain = binom.cdf(k=70, n=200, p=0.6)
print(bnk_retain)
## 8.60372025984695e-13 == 8.60372025984695 * 10 raised to -13
print(8.60372025984695 * (10 ** -4)) 
# =============================================================================
# 0.0008603720259846951 : if it was e-4
# 0.0000000000008603720259846951 : if it was e-13 

## Probability is extremely unlikely but never quite 0 (Read as chance of no more than 70 occurrences with 200 events and 60% chance of event occuring in any chance)

# =============================================================================
## Indeed it is hard to get zero here because we need 70 or less(in this case)
## https://stats.stackexchange.com/questions/319637/how-to-read-scientific-notation-output-numbers-that-include-e
print(-1.861246 * (10 ** -4))
## -0.0001861246

## Binom.sf comparison of 70 or more happening out of 200 events with a %60 chance of event happening in any occurence
print(binom.sf(k=70, n=200, p=0.6))
## 0.9999999999991396
print(1 - (binom.sf(k=70, n=200, p=0.6)) == binom.cdf(k=70, n=200, p=0.6))
## False 
print(1 - (binom.sf(k=70, n=200, p=0.6)))
## However, it's very close : 8.604228440844963e-13 ... compared to 8.60372025984695e-13


## Another Example - or fewer a cood indication of cdf
# =============================================================================
# Our task here is to calculate the probability that 10 or fewer residents in a specific town 
# with a population of 500 will answer yes to our question, "Do you have your housing?". 
# The probability that the answer will be positive is 40%.
# =============================================================================
twn_prb = binom.cdf(k=10, n=500, p=.4)
print(twn_prb)
## The probability is 5.23292013275132e-93
## As expected, super unlikely that we wouldn't get at least 11 out of 500 where any one answer is 40% yes




### Combine & Review

## Binom.pmf == Exactly (k) Successes given sample size (n) and probability of success (p)
# =============================================================================
# binom.pmf(k, n, p) :
#   - Calculate the probability to archive exactly k successes among n trials 
#     with the probability of success p
# =============================================================================

## Binom.sf == (k) or more Successes given sample size (n) and probability of success (p)
# =============================================================================
# binom.sf(k, n, p) :
#    - Calculate the probability to archive k or more successes among n trials 
#    with the probability of success p
# =============================================================================

## Binom.cdf == (k) or less Successes given sample size (n) and prbability of success (p)
# =============================================================================
# binom.cdf(k, n, p) :
#    - Calculate the probability to archive k or less successes among n trials 
#    with the probability of success p
# =============================================================================


# =============================================================================
# Calculate the probability that among 50 unique pictures, exactly 5 have a defect; the probability that a picture has a defect is 25%.
# Calculate the probability that at least 9(9 or more) employees are satisfied with their salary if we know that there are 20 workers in the project. The probability for the positive answer is 75% .
# Calculate the probability that 6 or fewer thefts this month will be revealed; we know that in the specific city, the amount of thefts is 10. The probability of revealing is 5%.
# =============================================================================


# Calculate the probability for pictures
experiment_1 = binom.pmf(k = 5, n = 50, p = 0.25)
# Calculate the probability for employees
experiment_2 = binom.sf(k = 9, n = 20, p = 0.75)
# Calculate the probability for thefts
experiment_3 = binom.cdf(k= 6, n = 10, p = 0.05)

# Print the probability for pictures
print("The probability is", experiment_1)
# Print the probability for employees
print("The probability is", experiment_2)
# Print the probability for thefts
print("The probability is", experiment_3)

## Readouts 
# =============================================================================
# The probability is 0.004937858735683688
# The probability is 0.9960578583359165
# The probability is 0.9999999180160156
# =============================================================================
















