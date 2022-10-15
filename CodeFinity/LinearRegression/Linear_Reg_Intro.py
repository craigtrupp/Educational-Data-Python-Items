#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:35:30 2022

@author: craigrupp
"""

## Welcome!
# =============================================================================
# Today we will start by investigating one of the most popular conceptions in machine learning - linear regression. 
# We will be digging into this simple supervised learning model using some well-known libraries of Python, which you probably already know.
# =============================================================================


## What is It?
# =============================================================================
# So what is regression? Before answering this question. 
# For example, we have done the research, got some data, then visualized it and plotted it on our graph.
# 
# We intuitively want to add a line to see what the trend is. But which one would best visualize our dependence? Blue? Green? Or maybe black?
# -- Note (Any Scatter plot where we may want to see a trend)
# =============================================================================

## Learning Model : Linear Regression
# =============================================================================
# To find the correct answer, we need to use a learning model - linear regression. 
# Let's find out the meaning of this method. Linear regression is an approach for modelling the relationship between variables that you operate in research, 
# finding mathematically the straight line to your data (if we are talking about two-dimensional graphs) to predict future values.
# =============================================================================


## Equation 
# =============================================================================
# y = kx + b
# Where 
#     b is the intercept 
#     k is the slope of the line 
#     x is an independent variable (input), 
#     y is our output. 
# Our goal is to find this k and b.
# =============================================================================

# Import the library
import matplotlib.pyplot as plt 

# Initialize the data
x = [8, 10, 9.2, 8.4, 9.1, 9.6, 8, 10.2, 9.3, 9.4, 9.9, 8.7]
y = [3.6, 5.4, 4.8, 3.9, 4.2, 5.2, 3.5, 5.5, 4.4, 4.7, 5.1, 3.7]

# Set the slope and the intercept
slope = 0.93
intercept = -3.97

# Build the line
def line(x):
   return slope * x + intercept

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# map(function, iterables)
cats = list(map(line, x))
print(cats) # Regression points for y plotted below after the scater [3.47, 5.33, 4.5859999999999985, 3.842000000000001, 4.493, 4.958, 3.47, 5.516, 4.679, 4.772, 5.237, 4.120999999999999]

# Similarly could apply the reression line by doing a comprehension on each index in x passed to the line function
cats_lc = [line(x) for x in x]
print(cats_lc) # [3.47, 5.33, 4.5859999999999985, 3.842000000000001, 4.493, 4.958, 3.47, 5.516, 4.679, 4.772, 5.237, 4.120999999999999]
# Add titles to axes
ax = plt.gca()
ax.set_xlabel('Cat height (inches)')
ax.set_ylabel('Cat weight (kg)')

# Visualize our data
plt.scatter(x, y)
plt.plot(x, cats)
plt.show()



## How's it Working?
# =============================================================================
# We need to draw the line in such a way that it best determines the dependence of our variables. 
# In other words, the points should lie as closely as possible around our straight line. The method for finding a straight line is as follows:
#     
# 1) Let's measure how far the points are from a random line.
# 2) Minimizing the distance to each constructed line, we find the desired one.
# =============================================================================
    
## Residual - Step 1
# =============================================================================
# First, what will we consider the distance from a point to our line? It’s the distance between data points and the fitted line calculated by axis y.
# These residuals are indicated by the dashed violet vertical lines which show the distance from the observed point to the fitted line 
# =============================================================================

## Ordinary Least Squares - Step 2
# =============================================================================
# In the second step we are minimizing the distance and finding the line where the sum of squared residuals (SSR) is minimal. 
# This approach is called the method of ordinary least squares.
# 
# Why exactly squares? The squares help avoid contraction due to sign difference, and any strong deviations are reflected more materially in the result. 
# Moreover, it is also helpful in mathematical calculations of the minimum of these distances.
# =============================================================================

## Task
# =============================================================================
# Continuing the previous task, try to show also the dependence of the weight of Abyssinian cats on their height, 
# knowing that the slope and the intercept are 0.99 and 4.7, respectively.
# =============================================================================

# Initialize the data
x = [8, 10, 9.2, 8.4, 9.1, 9.6, 8, 10.2, 9.3, 9.4, 9.9, 8.7] 
y = [3.6, 5.4, 4.8, 3.9, 4.2, 5.2, 3.5, 5.5, 4.4, 4.7, 5.1, 3.7] 

# The line shows the dependence of the height of cats on their weight
def on_weight(x): 
   return 0.93 * x - 3.97 

# The line shows the dependence of the weight of cats on their height
def on_height(y):
   return 0.99 * y + 4.7 

# Define lines 
height_on_weight = list(map(on_weight, x)) 
weight_on_height = list(map(on_height, y)) 

# Add titles to axes 
ax = plt.gca() 
ax.set_xlabel('Cat height (inches)') 
ax.set_ylabel('Cat weight (kg)') 

# Visualize our data 
plt.scatter(x, y) 
plt.plot(x, height_on_weight, c='g', label='Height On Weight') 
plt.plot(weight_on_height, y, c='y', label='Weight On Height')
plt.legend() 
plt.show()





## Build Linear Regression - stats.lingress()
# =============================================================================
# For this example, we will use a scientific computation library SciPy, to import stats. 
# Using the method stats.lingress() we can get the most important linear regression parameters for the given dataset (x and y arrays).
# =============================================================================
# =============================================================================
# Getting bigger, cats start to eat more. Let's see how these values are dependent. 
# We have a dataset in which the number of calories the cat eats every day at a certain weight is indicated (array x - weight, y - number of calories).
# =============================================================================
# Import stats library
from scipy import stats 
# Initialize the data
x = [1.8, 2.24, 11.2, 7, 4.2, 9.3, 10.3, 6.3, 1.4, 5.8, 1.1, 4.3]
y = [111, 130, 450, 320, 195, 360, 402, 272, 85, 263, 105, 237]

# Get the linear regression parameters 
slope, intercept, r, p, std_err = stats.linregress(x, y)

# The line shows the dependence of the number of calories on cats' weight 
def on_weight(x):
  return slope * x + intercept

# Define the line 
feed_on_weight = list(map(on_weight, x))

# Add titles to axes
ax = plt.gca()
ax.set_xlabel('Cat weight (kg)')
ax.set_ylabel('Cat ration (calories)')

# Visualize our data 
plt.scatter(x, y)
plt.plot(x, feed_on_weight)
plt.show()



## Working w/DataSet - Scikit-learn dataset : import load_wine
# =============================================================================
# Scikit-learn comes with a few small standard datasets that do not require downloading and are very helpful for learning new models in machine learning. 
# In this course, we will become high-class sommeliers and determine the quality of wine using statistics and regression. 
# Wine recognition dataset provides a large variety of characteristics of wine: Alcohol, Ash, Magnesium, Total phenols, Color intensity, and so on.
# =============================================================================
import pandas as pd
from sklearn.datasets import load_wine

# Load dataset
wine = load_wine()
print(type(wine)) # <class 'sklearn.utils._bunch.Bunch'>
print(type(wine['feature_names'])) # <class 'list'>

# Configure pandas to show all features
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# Convert data to a dataframe to view it properly 
## Looks like the bunch object in the wine variable holds key like json attributes we can declare the frame with
data = pd.DataFrame(data = wine['data'], columns = wine['feature_names'])
print(data.head())


## Visualize data about alcohol consistency in the set
data.hist(column = 'alcohol', bins = 15) 
plt.show()




### Correlation - Pearson Coefficient
# =============================================================================
# The strength of the relationship can be quantified by correlation. It means that the dataset with a weak relationship has a small correlation value, 
# and with a strong relationship, the large one. The maximum value of correlation is 1, and the minimum is -1. 
# It is also called the correlation coefficient or the Pearson correlation coefficient, often denoted with the letter r (called Pearson’s r)
# =============================================================================
# =============================================================================
# We have a correlation value = 1 when the straight line (which we have told in the previous section) goes through each point of the dataset with a positive slope. 
# A similar situation is when a correlation value - 1. It happens when the straight line goes through each dataset point with a negative slope.
# =============================================================================
# Initialize the data
x = [1.8, 2.24, 11.2, 7, 4.2, 9.3, 10.3, 6.3, 1.4, 5.8, 1.1, 4.3]
y = [111, 130, 450, 320, 195, 360, 402, 272, 85, 263, 105, 237]

# Get the linear regression parameters 
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Add titles to axes
ax = plt.gca()
ax.set_xlabel('Cat weight (kg)')
ax.set_ylabel('Cat ration (calories)')

# Print the Pearson coefficient
print('Correlation coefficient =', r)

# Visualize our data 
plt.scatter(x, y)
plt.show()


## Correlation Matrix
# =============================================================================
# To explore the relationships between all the columns, we can use a correlation matrix. 
# It finds pairwise correlation coefficients of all columns(that's why the matrix is symmetric
# =============================================================================
# =============================================================================
# Seaborn's heatmap can be leveraged for a like visual correlation matrix
# =============================================================================
import seaborn as sns
# Defining the matrix
matrix = data.corr().round(2)
print(type(matrix))

## Top/Lowest Correlation Value for Each DataFrame Column (Not including itself - load into dictionary) - Correlation Pairs (Highest & Lowest )
highest_lowest_correlations = {}
# Loop through data correlation matrix
for index, row in matrix.iterrows():
    # Set row.name to object along with an empty list to append top positive & negative value
    highest_lowest_correlations[row.name] = []
    temp_obj = {}
    # Loop through row  which returns as a series
    for key, val in row.iteritems():
        # ignore row's own column matrix value of 1
        if key != row.name:
            # Add column value to temp_object with col_name:val for all other series values (from row being looped through)
            temp_obj[key] = val
    # Add Max Value Key & Value - use lambda with key argument to get the top column/key correlation value
    max_key = max(temp_obj, key = lambda x: temp_obj[x])
    max_value = max(temp_obj.values())
    highest_lowest_correlations[row.name].append({max_key:max_value})
    # Add Min Value Key & Value - use lambda with key argument to get the min column/key correlation value (lowest negatrive corr value)
    min_key = min(temp_obj, key = lambda x: temp_obj[x])
    min_value = min(temp_obj.values())
    highest_lowest_correlations[row.name].append({min_key:min_value})
    
print(highest_lowest_correlations) # Each key in the object below has their respective highest and lowest correlation value from the corr matrix
# =============================================================================
# {'alcohol': [{'proline': 0.64}, {'alcalinity_of_ash': -0.31}], 'malic_acid': [{'alcalinity_of_ash': 0.29}, {'hue': -0.56}], 
# 'ash': [{'alcalinity_of_ash': 0.44}, {'hue': -0.07}], 'alcalinity_of_ash': [{'ash': 0.44}, {'proline': -0.44}],
# 'magnesium': [{'proline': 0.39}, {'nonflavanoid_phenols': -0.26}], 'total_phenols': [{'flavanoids': 0.86}, {'nonflavanoid_phenols': -0.45}], 
# 'flavanoids': [{'total_phenols': 0.86}, {'nonflavanoid_phenols': -0.54}], 'nonflavanoid_phenols': [{'alcalinity_of_ash': 0.36}, {'flavanoids': -0.54}], 
# 'proanthocyanins': [{'flavanoids': 0.65}, {'nonflavanoid_phenols': -0.37}], 'color_intensity': [{'alcohol': 0.55}, {'hue': -0.52}], 
# 'hue': [{'od280/od315_of_diluted_wines': 0.57}, {'malic_acid': -0.56}], 'od280/od315_of_diluted_wines': [{'flavanoids': 0.79}, {'nonflavanoid_phenols': -0.5}], 
# 'proline': [{'alcohol': 0.64}, {'alcalinity_of_ash': -0.44}]}
#         
# =============================================================================
print(highest_lowest_correlations.items()) # dict_items([('alcohol', [{'proline': 0.64}, {'alcalinity_of_ash': -0.31}]) - Use for Indexing to get positive corr values below
# Sep List for High Correlation Values (grabs the first value in each key's list holding top positive and negative correlation)
highest_values = [x[1][0] for x in highest_lowest_correlations.items()]
print(highest_values)
# [{'proline': 0.64}, {'alcalinity_of_ash': 0.29}, {'alcalinity_of_ash': 0.44}, {'ash': 0.44}, {'proline': 0.39}, 
# {'flavanoids': 0.86}, {'total_phenols': 0.86}, {'alcalinity_of_ash': 0.36}, {'flavanoids': 0.65}, {'alcohol': 0.55}, 
# {'od280/od315_of_diluted_wines': 0.57}, {'flavanoids': 0.79}, {'alcohol': 0.64}]

# Max value in list of dictionaries (highest_values variable above which holds the highest correlation value for each key above)
positive_cor_top_value_key = max(highest_values, key=lambda x: list(x.values()))
print(positive_cor_top_value_key) # {'flavanoids': 0.86}
# dict object not subscriptable so must mutate to list then simply just grab the only list value
positive_cor_top_value = list(positive_cor_top_value_key.values())[0]
print(positive_cor_top_value) # 0.86

## Find all Columns/Keys that have a correlation equal to positive_cor_top_value of 0.86 (Should be at least 2 - will get the same key/pair reversed from the matrix) and any other pairs that match that top value
top_correlation_pairs = []
for key, val in highest_lowest_correlations.items():
    # Need to Grab first Index from each key for max checking val[0] is just the first index for each value in the dictionary / Mutate type for easier comparison below
    max_val_col = list(val[0].values())[0]
    print(max_val_col)
    if max_val_col == positive_cor_top_value:
        top_correlation_pairs.append({key:val[0]})
    
print(top_correlation_pairs) 
# [{'total_phenols': {'flavanoids': 0.86}}, {'flavanoids': {'total_phenols': 0.86}}]

## Cool! Let's get the Negative (Should be fairly easier now lol)

# Grabbing negative correlation pairs from object created through matrix/series pairs
lowest_values = [x[1][1] for x in highest_lowest_correlations.items()]
print(lowest_values)
# [{'alcalinity_of_ash': -0.31}, {'hue': -0.56}, {'hue': -0.07}, {'proline': -0.44}, {'nonflavanoid_phenols': -0.26}, {'nonflavanoid_phenols': -0.45}, {'nonflavanoid_phenols': -0.54}, {'flavanoids': -0.54}, {'nonflavanoid_phenols': -0.37}, {'hue': -0.52}, {'malic_acid': -0.56}, {'nonflavanoid_phenols': -0.5}, {'alcalinity_of_ash': -0.44}]
negative_cor_value_most_corr_key = min(lowest_values, key=lambda x: list(x.values()))
print(negative_cor_value_most_corr_key)
# {'hue': -0.56}
negative_cor_values_most_corr_val = list(negative_cor_value_most_corr_key.values())[0]
print(negative_cor_values_most_corr_val)

neg_corr_pairs = []
for key, val in highest_lowest_correlations.items():
    # Grab Second index from each key for min checking val[1] to get negative index of each row's max found pair in the matrix
    min_val_col_corr = list(val[1].values())[0]
    # print(min_val_col_corr
    if min_val_col_corr == negative_cor_values_most_corr_val:
        # print(key, '\n', val) : [{'alcalinity_of_ash': 0.29}, {'hue': -0.56}] reminder getting the entire original dictionary value (including top correlated pair for that row/key)
        neg_corr_pairs.append({key:val[1]})
        
print(neg_corr_pairs)
# [{'malic_acid': {'hue': -0.56}}, {'hue': {'malic_acid': -0.56}}]

# Print results
print('the greatest positive correlation coefficient was between ', str(top_correlation_pairs))
# the greatest positive correlation coefficient was between  [{'total_phenols': {'flavanoids': 0.86}}, {'flavanoids': {'total_phenols': 0.86}}]
print(str(list([dt.keys() for dt in top_correlation_pairs]))) # [dict_keys(['total_phenols']), dict_keys(['flavanoids'])]
print('the value of correlation is = ', positive_cor_top_value) # the value of correlation is =  0.86

print('the greatest negative correlation coefficient was between ', str(neg_corr_pairs))
# the greatest negative correlation coefficient was between  [{'malic_acid': {'hue': -0.56}}, {'hue': {'malic_acid': -0.56}}]
print('the value of correlation is = ', negative_cor_values_most_corr_val )
# the value of correlation is =  -0.56

# Set scale and visuale data
sns.set(rc = {'figure.figsize':(20,10)})
sns.heatmap(matrix, annot=True)
plt.show()


## Get key with maximum value in Dictionary
Tv = {'BreakingBad':100,'GameOfThrones':1292,'TMKUC': 88}
 
Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)



## Calculating the Pearson Coefficient Using NumPy and Pandas

## np.corrcoef()
# =============================================================================
# Let's look at how we can calculate the correlation coefficient if our data's type is np.array. 
# The library has many statistics routines which simplify the calculations. We will use the method np.corrcoef(). 
# It works with 2 arrays of the same length of our data:
# =============================================================================
import numpy as np
# Define np.arrays
x = np.array([1, 2, 3, 5, 7, 8, 10, 11, 13, 15])
y = np.array([2, 4, 7, 8, 10, 15, 20, 21, 23, 30])

# Find correlation
r = np.corrcoef(x, y)
print(r)
# =============================================================================
# [[1.         0.98661904]
#  [0.98661904 1.        ]]
# =============================================================================

## Array Broken Down (Equal on Diagnoals with itself for Corr Value)
# [[x , y]
#  [y, x]]

# =============================================================================
# The upper right value corresponds to the correlation coefficient for y and x, while the lower-left value is the correlation coefficient for x and y. 
# These values we will always need. The other ones are the correlation coefficients between x and x, y and y. They are always equal to one.
# =============================================================================

## Pearson coefficient
print(np.corrcoef(x, y)[0,1]) # 0.9866190374718473



## Pandas Usage
# =============================================================================
# Pandas correlation calculations also has a function to calculate the correlation coefficient for two of the same length Series objects. 
# You can use .corr() method:
# =============================================================================

import pandas as pd

# Define series
x = pd.Series([1, 2, 3, 5, 7, 8, 10, 11, 13, 15])
y = pd.Series([2, 4, 7, 8, 10, 15, 20, 21, 23, 30])

# Print correlation coeffitients
print(x.corr(y))
print(y.corr(x))

# =============================================================================
# 0.9866190374718473
# 0.9866190374718473
# =============================================================================



## Task
# =============================================================================
# You have the initial dataset of Abyssinian cats' weight and height (x and y arrays, respectively). 
# Find the correlation coefficient between x and y using all functions
# =============================================================================
# Initialize the data
x = [8, 10, 9.2, 8.4, 9.1, 9.6, 8, 10.2, 9.3, 9.4, 9.9, 8.7]
y = [3.6, 5.4, 4.8, 3.9, 4.2, 5.2, 3.5, 5.5, 4.4, 4.7, 5.1, 3.7]

# Find and print the correlation coefficient with np.arrays
np_x = np.array(x)
np_y = np.array(y)
print(np.corrcoef(np_x, np_y)[0,1])

# Find and print the correlation coefficient with pd.Series 
pd_x = pd.Series(x)
pd_y = pd.Series(y)
print(pd_x.corr(pd_y))



## Last Section / Task
# =============================================================================
# You have the dataset about Abbisian cats where the number of calories the cat eats every day of a certain weight 
# is indicated (array x - weight, y - number of calories).
# =============================================================================
# Initialize the data
x = [1.8, 2.24, 11.2, 7, 4.2, 9.3, 10.3, 6.3, 1.4, 5.8, 1.1, 4.3]
y = [111, 130, 450, 320, 195, 360, 402, 272, 85, 263, 105, 237]

# Add titles to axes
ax = plt.gca()
ax.set_xlabel('Cat weight (kg)')
ax.set_ylabel('Cat ration (calories)')

# The line shows the dependence between x and y 
def line(x):
  return slope * x + intercept

# Get the linear regression parameters
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Print results
print(f"Correlation coefficient of : {r}")
print(f"Slope of : {slope}")
print(f"Intercept of : {intercept}")

# Find the line
built_line = list(map(line, x))

# Visualize the data
plt.scatter(x, y)
plt.plot(x,built_line)
plt.show()

























