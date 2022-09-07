#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 08:46:55 2022

@author: craigrupp
"""

# =============================================================================
# CAC formula:
# 
# CAC  = Sales & Marketing Expense / Number of New Customers
# =============================================================================

import pandas as pd

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/783d7288-e86b-4b89-9966-a2fe97995277/section_3_dataset_upd.csv', index_col=0)
print(df.head(2))
print(df.describe())
# Sum all expenses
expenses = df['cost'].sum()
# Find the number of rows
customers_number = df.shape[0]
# Define the CAC variable
CAC = expenses/customers_number
# Print the CAC value in 0.00 format
print('CAC =', round(CAC, 2))

# =============================================================================
#   customer_id    cost  money_spent       day  holiday
# 0           21  151.73        65.57    Friday    False
# 1           26  153.33        60.43  Thursday    False
#        customer_id         cost  money_spent
# count  4184.000000  4184.000000  4184.000000
# mean     38.346080   126.905968   101.975600
# std      38.484676    30.416955   130.531106
# min       0.000000     0.000000    40.500000
# 25%      11.000000   106.925000    60.375000
# 50%      27.000000   131.300000    66.150000
# 75%      53.000000   151.282500    72.710000
# max     344.000000   172.430000   799.000000
# CAC = 126.91
# =============================================================================


# =============================================================================
# Count the number of the costly customers:
# Set the condition if the value in the 'cost' column is greater than the value in the 'money_spent' column
# Use unique customers to find the metric
# Print the number of the costly customers.
# Find the percentage of costly customers using the formula.
# Print the result of countings in the 0.00 format.

# Sometimes we don't receive as much as we spend. The same with some customers in our DataFrame. We do spend more money to 'buy' this customer, 
# but we don't receive the the same amount of money.
# Let's find the percentage of these customers!
# =============================================================================
import pandas as pd
print(df.head(2))
# Count the number of the costly customers
customer_counter = df[df['cost'] > df['money_spent']].customer_id.nunique() 
customer_counter_2 = len(df[df['cost'] > df['money_spent']].customer_id.value_counts())
# Print the number of the costly customers & total customers
# col.nunique() pulls a count of all unique values (think distinct) - also achievable with a len of the unique value_counts
print('The number of costly customers', customer_counter)
print('The number of costly customers', customer_counter_2)
print('Total customers', df.customer_id.nunique())
# Find the percentage of costly customers
  
percentage_customer = (customer_counter * 100) / df.customer_id.nunique()
  
# Print the result in 0.00 format
  
print('The percentage of costly customers', round(percentage_customer, 2), '%')




# =============================================================================
# Your performance was super!
# 
# You need to count the percentage of organic traffic.
# 
# Organic traffic is those visitors that land on your website from unpaid sources, aka essentially free traffic.
# =============================================================================
import pandas as pd

# Find the number of the organic traffic
organic_counter = df[df.cost == 0].customer_id.nunique() 

# Print the number of the organic traffic
print('The number of organic traffic', organic_counter)

# Find the percentage of organic customers
percentage_organic = (organic_counter * 100) / df.customer_id.nunique()

# Print the result in 0.0 format
print('The percentage of organic customers', round(percentage_organic,1), '%')

# =============================================================================
# 
# The number of organic traffic 1
# The percentage of organic customers 0.5 %
# =============================================================================



# =============================================================================
# You may recognize the column 'money_spent' that corresponds to the amount of money the user spent and gained. 
# In this chapter, we will find if there is any dependence between the day of the week and the amount of money we have!
# =============================================================================


import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/783d7288-e86b-4b89-9966-a2fe97995277/section_3_dataset_upd.csv', index_col=0)

# Group the df
df = df[['day', 'money_spent']].groupby(['day']).mean().reset_index()
print(df.head(2))
# Create barplot
sns.barplot(data = df, x = 'day', y = 'money_spent')
# Output barplot
plt.xticks(rotation=45)
plt.show()

# Run in block to see bargraph for grouped by data averages



# =============================================================================
# Is Our Project Profitable? ROI 1/2
# Is our project profitable? To figure this out, you can calculate one simple metric titled ROI; the formula is:
# 
# roi = (Earning - losses) / losses
# 
# Earnings, the sum of the column 'money_spent'.
# Losses, the sum of the column 'cost'.
# =============================================================================


df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/783d7288-e86b-4b89-9966-a2fe97995277/section_3_dataset_upd.csv')

# Calculate the sum of cost
cost_sum = df['cost'].sum()
# Calculate the sum of money_spent
spent_sum = df.money_spent.sum()

# Calculate ROI
ROI = ((spent_sum - cost_sum)/cost_sum)*100

# Output ROI
print(ROI)

# =============================================================================
# -19.644756245106056 - YIKES!
# 
# =============================================================================




# =============================================================================
# As you can recognize from the previous chapter, we have some problems with ROI in general; 
# we received -19.644756245106056%. Unfortunately, we suffer losses. 
# In this case, we must dive deeper and find the reason.
# 
# The next step of our research is to check if we have unprofitable days.
# =============================================================================

import pandas as pd

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/783d7288-e86b-4b89-9966-a2fe97995277/section_3_dataset_upd.csv')

# Group data
df = df[['day', 'cost', 'money_spent']].groupby('day').sum().reset_index()

# Create column ROI
df['ROI'] = round(((df['money_spent'] - df['cost'])/ df['cost'])*100, 2)

print(df)


## Visualize ROI
sns.barplot(data = df, x = 'day', y = 'ROI')
# Output barplot
plt.xticks(rotation=45)
plt.show()




































