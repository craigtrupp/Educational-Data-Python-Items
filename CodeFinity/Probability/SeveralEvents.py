#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:21:37 2022

@author: craigrupp
"""

## Add Probabilities
# Where can I use it?
# =============================================================================
# In situations when either one of the events should happen. 
# Events should be absolutely independent.
# P = P(quantity of desired outcomes (n) / the quantity of all outcomes (m))1 + P(n/m)2 + P(n/m)3 ...etc
# =============================================================================
# =============================================================================
# 
# Consider you are going to win a lottery. Lottery tickets are kept in a box; there are 10 $500 winning tickets, 
# 15 $11 000 winning tickets, 3 $15 000 winning tickets, and 2 losing lottery tickets.
# 
# Calculate the probability of winning at least $10 000 or, in another wording, the probability of getting an $11 000 winning ticket or a $15 000 winning ticket.
# 
# Calculate the probability of getting an $11 000 winning ticket.
# Calculate the probability of getting a $15 000 winning ticket.
# Calculate the probability of winning at least $10 000.
# =============================================================================
Eleven = 15/30
Fifteen = 3/30
print(Eleven + Fifteen, f"There is a {100 * (Eleven + Fifteen)}% chance of at least winning $10,000")
## 0.6 There is a 60.0% chance of at least winning $10,000



## Calculate Connected Probabilities
# =============================================================================
# Imagine that we have 5 bananas, 3 lemons, 2 yellow tomatoes, 3 red tomatoes, and 7 green apples.
# Calculate the probability of getting a fruit or yellow item.
# =============================================================================
# =============================================================================
# yellow items (yellow tomato, lemon, banana) 
# blue represents all fruits (bananas, lemon, apple). 
# But fruit can be yellow(banana, lemon). We can see the intersection of this too circle, 
# which means that if we just add two probabilities, we will calculate yellow fruits twice, 
# so it is crucial to subtract the probability of getting yellow fruit.
# P = P(yellow_item)1 + P(fruit)2 - P(yellow_fruit)
# =============================================================================
yellow_items = 10/20
fruit_items = 15/20
yellow_fruit = 8/20

fruit_or_yellow_prb = (yellow_items + fruit_items) - yellow_fruit
print(fruit_or_yellow_prb, f"There is about a : {round(fruit_or_yellow_prb * 100,3)}% of getting either a fruit or yellow item")
## 0.85 There is about a : 85.0% of getting either a fruit or yellow item

# =============================================================================
# Let's imagine one situation that may be real for you. You have a tasty basket with:
# 
# 5 cookies with a cherry jam,
# 5 chocolate cookies,
# 10 chocolate candies,
# 5 chocolate bars,
# 15 biscuits,
# 10 bottles of lemonade.
# =============================================================================
# =============================================================================
# Calculate the probability that you will randomly pull out an item 
# that includes chocolate, or a cookie. (Don't double count chocolate cookies!)
# =============================================================================
# Calculate the probability of getting cookie
P_cookie = 10 / 50
# Calculate the probability of getting chocolate sweets
P_chocolate = 20 / 50
# Calculate the probability of getting chocolate cookie
P_chocolate_cookie = 5/50

# Calculate the resulting probability
P_choc_cook = P_cookie + P_chocolate - P_chocolate_cookie

print("The probability is:", P_choc_cook)
## The probability is: 0.5000000000000001
print(f"a {int(round(100*P_choc_cook,0))}% chance")
## a 50% chance


## Multiply probabilities
# =============================================================================
# Sometimes it is impossible to pick one event, hence, 
# we should refer to the multiplication rule for independent events.
# 
# Independent events mean that the occurrence of one event doesn't 
# depend on another event like flipping two coins or rolling two dies.

# Used when we have certainty of more than one event (n=desired, m=total ) per independent event
# P = n/m * n/m
# =============================================================================
# =============================================================================
# Imagine the situation where you learned only 2 topics of 5 for the math exam and 
# only 1 of 7 for the English exam. To get a high result, you need to succeed in English and Math.
# 
# Calculate the probability that you will get the right ticket for the exam in Math and English
# =============================================================================
# Calculate the probability of success in Math
P_Math = 2 / 5
# Calculate the probability of success in English
P_English = 1 / 7

# Calculate the probability of success in both exams
P_math_eng = P_Math * P_English

print("The probability is", P_math_eng, f"a {round(100*P_math_eng, 5)}% chance")
## The probability is 0.05714285714285714 a 5.71429% chance



## Dependent probabilities
# =============================================================================
# Example:
# 
# Imagine that we have 4 blue balls in the basket, 4 green balls, 2 red ones and 3 yellow balls.
# Calculate the probability of pulling out when we 
# ! ) pull out the blue ball first, 
# 2 ) followed by the green one, 
# 3) and finally the red.
# 
# P = 4/13 * 4/12 * 2/11 = 0.01864
# =============================================================================
# =============================================================================
# In a card game, to win we have to get from the deck of cards first the ace, then the queen, then the nine. 
# Calculate the probability of getting such a result.
# =============================================================================
# Calculate the probability to get the ace
P_Ace = 4 / 52
# Calculate the probability to get the queen
P_Queen = 4 / 51 
# Calculate the probability to get the nine
P_Nine = 4 / 50

# Calculate the probability to win the game
P_CardWin = P_Ace * P_Queen * P_Nine
print("The probability is", P_CardWin, f"{round(P_CardWin * 100,3)}% chance")
## The probability is 0.00048265460030165913 0.048% chance


## Law of Total Probability
# =============================================================================
# exhaustive events : when at least one event must happen
# 
# The simplest and the most evident example is tossing a coin. 
# The probability of receiving head or tail is 50%, but together they result in 100%(all outcomes).
# In other words, the events are exclusive.
# 
# =============================================================================
## Example
# =============================================================================
# Imagine that we have three boxes. 
# The first one contains 7 red balls, the second one contains 5 green balls 
# and the third one contains 4 green balls and 3 red balls. 
# Calculate the probability that we will randomly pull out red ball.

#   To find it we should multiply the probability to pick a specific box 
#   by the probability to pull out the box from this column.
#   P(red) = RBag(1/3 * 1) + GBag(1/3 * 0) + RGBag(1/3 * 3/7)
# =============================================================================
red_ball_prob = (1/3 * 1) + (1/3 * 0) + (1/3 * 3/7)
print(red_ball_prob, f'Total probability of Example scenario above : {100 * round(red_ball_prob,4)}')
## 0.47619047619047616 Total probability of Example scenario above : 47.620000000000005

# Exercise
# =============================================================================
# Imagine that we have three chocolates, the first one with 3 red berries, the second one with 5 orange berries, 
# and the third one with 2 red berries and 4 orange berries. 
# Calculate the probability that when we break off a piece with a berry from a random chocolate bar, there will be orange berry.
# =============================================================================

# The probability that we will randomly pick the first chocolate
P_1 = 1 / 3
# The probability that we will randomly pick the second chocolate
P_2 = 1 / 3
# The probability that we will randomly pick the third chocolate
P_3 = 1 / 3 

# The probability that orange berries in the first chocolate
P_1_orange = 0
# The probability that orange berries in the second chocolate
P_2_orange = 1
# The probability that orange berries in the third chocolate
P_3_orange = 4 / 6

# Apply the law of total probability
P_orange = P_1 * P_1_orange + P_2 * P_2_orange +  P_3 * P_3_orange
print("The probability is", P_orange, f"{round(100*P_orange, 3)}% chance of breaking off chocolate w/orange")
## The probability is 0.5555555555555556 55.556% chance of breaking off chocolate w/orange



## Bayes Theorem
# =============================================================================
# The theorem helps figure out the probability that one event will happen, 
# considering that another statistically related one happened.
# =============================================================================

# Example
# =============================================================================
# There are 600 red balls and 900 green balls. 
# We know that among all balls, 5% of red balls have a defect and 20% of green balls have a defect too. 
# Randomly we pulled out a ball with a defect, calculate the probability that it relates to the red ones.
# 
# Red Probability : 600/1500 = .4   || Green Probability : 900/1500 = .6   == Exhaustive Events 
# Probability to pull a ball with a defect that's red (Red : .4 * .05 == Percent total for red ball times percent of possible defect)
# Probability to pull a ball with a defect that's green (Green : .6 * .2 == Percent total for pulling green ball and possibility of defect'
# (0.4 * 0.05 + 0.6 * 0.2 == 0.14)
# 
# Probability that a random ball w/a defect belongs to red ones:
# (0.4 * 0.05 / 0.14 == 0.14285)
# 
# #Formula
# P(A|B) = P(B|A) * P(A) / P(B)
#     * P(A|B) = Probability that event A will occur if event B will occur 
#     * P(B|A) = Probability that event B will occur if event A will occur
#     * P(A) = Probability that event A will occur (Probability of red defect)
#     * P(B) = Probability that event B will occur (Randomly pulled ball w/defect)
# =============================================================================

# Exercise
# =============================================================================
# Assume that you have a box with red and green balls. 
# There are 600 red balls and 900 green balls. 
# You know that among all balls 5% of red balls have a defect and 20% of green balls have a defect too. 
# Randomly you pulled out a ball with a defect; calculate the probability that it relates to the green ones.
# =============================================================================
P_red = 600 / 1500
# Calculate the probability to pull out the green ball
P_green = 900/1500

P_red_defect = 0.05
P_green_defect = 0.20

# Calculate the probability that you randomly pull out a ball with a defect
P_random_defect = P_red * P_red_defect + P_green * P_green_defect
# Calculate the probability that a random ball belongs to green ones
P_defect_belong_green = (P_green * P_green_defect)/P_random_defect

print("The probability is", P_defect_belong_green, f"Should a randomly picked ball with a defect be picked, the percent chance it was green is that would be green is : {round(100 * P_defect_belong_green, 4)}%")
## The probability is 0.857142857142857 
## Should a randomly picked ball with a defect be picked, the percent chance it was green is that would be green is : 85.7143%



## Challenge
# =============================================================================
# Imagine that we decided to conduct medical research. 
# You gathered data about two groups of people: 750 people with heart problems and 800 people with chronic stomachache.
# You know that 7% of interviewed from the first group have diabetes; meanwhile, 12% of respondents from the second group have diabetes too.
# Calculate the probability that a randomly selected person with diabetes has a chronic stomachache.
# =============================================================================
# Probability that randomly selected person has heart problem
P_heart = 750 / 1550
# Probability that randomly selected person has stomachache
P_stomach = 800/1550

P_heart_diabetes = 0.07
P_stomach_diabetes = 0.12

# Probability that you randomly select a person that has diabetes
P_random_diabetes = P_heart * P_heart_diabetes + P_stomach * P_stomach_diabetes

# Randomly selected person with diabetes has chronic stomachache
P_diabetes_belong_stomach = (P_stomach * P_stomach_diabetes)/P_random_diabetes

print("The probability is", P_diabetes_belong_stomach)

### Given diabetes (the probability that event B occurred) what are the odds the individual has chronic stomache aches (probability of picking a stomach ache * percent that percon has diabetes)



