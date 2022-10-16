#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:31:31 2022

@author: craigrupp
"""

## Building the Regression Model Based on Several Variables

## Basis - Equation for MLV Reg
# =============================================================================
# Often we will need to make predictions based not on one but on several characteristics at once.
# 
# For example, predict the length of a cat's tail knowing its weight and height. 
# In such a case our equation looks like this:
# 
# tail_length = a + b * cat_weight + c * cat_height
# 
# Here we need to find we have to find already three unknown variables 
# (the intercept a, coefficients b and c).
# =============================================================================

## Multivariate regression
# =============================================================================
# So multivariant regression is the way to predict a value based on two or more variables. 
# Let’s indicate the number of flavanoids based on the number of total phenols and nonflavanoid phenols. 
# Dealing with these two characteristics we will use methods from the previous section to find the best model and get missing parameter
# =============================================================================

## Task
# Let’s indicate the number of total phenols based on the number of flavanoids and nonflavanoid phenols

# Import the libraries
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
wine = load_wine()

# Configure pandas to show all features
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# Define the DataFrame
data = pd.DataFrame(data = wine['data'], columns = wine['feature_names'])
print(data.columns)

# Define the target
data['total_phenols'] = wine.target

# Prepare the data
X2 = data[['flavanoids', 'nonflavanoid_phenols']]
Y = data['total_phenols']

# Train and fit the model
X2_train, X2_test, Y_train, Y_test = train_test_split(X2, Y, test_size=0.3, random_state=1)
model2 = LinearRegression()
model2.fit(X2_train, Y_train)

# Print results
print(model2.intercept_)
print(model2.coef_)

## Intercept and respective (slopes/coefficients for explanatory variables = X2 dataframe above)
# =============================================================================
# 2.0649392463850473
# [-0.61399485  0.34456086]
# =============================================================================


## Evaluate Multi-Variate Model

# Rule of Thumb
# =============================================================================
# As a general rule, the more features a model includes, the lower the MSE (RMSE) and 
# MAE will be. However, be careful about including too many features. 
# Some of them may be extremely random, degrading the model's interpretability.
# =============================================================================

## First need to predict our test vallue set from train_test
y_test2_predictions = model2.predict(X2_test)

# Calculate the MSE 
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(Y_test, y_test2_predictions).round(2)
print(MSE)

# Calculate the R-squared
from sklearn.metrics import r2_score
r_squared = r2_score(Y_test, y_test2_predictions).round(2)
print(r_squared)

## MSE & r2 (coefficient of determination) - Not too Bad of a Fit
# =============================================================================
# 0.14
# 0.77
# =============================================================================


## Task
# =============================================================================
# Let’s indicate the number of nonflavanoid phenols based on the number of flavanoids, 
# total phenols and evaluate our model.
# =============================================================================

# Load in dataset (set new target )
wine_2 = load_wine()

# Configure pandas to show all features
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# Define the DataFrame
data = pd.DataFrame(data = wine_2['data'], columns = wine_2['feature_names'])

# Define the target
data['nonflavanoid_phenols'] = wine_2.target

# Prepare the data
X2_2 = data[['flavanoids', 'total_phenols']]
Y_2 = data['nonflavanoid_phenols']

# Split the data, initialize and fit the model
X2_2train, X2_2test, Y_2train, Y_2test = train_test_split(X2_2, Y_2, test_size=0.3, random_state=1)
model2 = LinearRegression()
model2.fit(X2_2train, Y_2train)

# Calculate the MAE
y_test_predicted2 = model2.predict(X2_test)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(Y_2test, y_test_predicted2).round(2)) ## 0.31
print((Y_2test - y_test_predicted2)[0:4])
# =============================================================================
# 161    0.182443
# 117    0.218516
# 19    -0.140454
# 69    -0.312174
# =============================================================================
## abs usage
print(abs(Y_2test - y_test_predicted2)[0:4])
# =============================================================================
# 161    0.182443
# 117    0.218516
# 19     0.140454
# 69     0.312174

## absolute is iterating over return arithmetic pandas series from test - predictions 
# =============================================================================
print(abs(Y_2test - y_test_predicted2).mean()) ## 0.3148651629286172
print(round(abs(Y_2test - y_test_predicted2).mean(), 2)) ## 0.31


# Calculate the R-squared
from sklearn.metrics import r2_score
r_squred = r2_score(Y_2test, y_test_predicted2)
print(r_squared.round(2)) ## 0.77

resids_2 = Y_2test - y_test_predicted2
print(len(resids_2), type(resids_2)) # 54 <class 'pandas.core.series.Series'>
# sum squared mean of the residuals
rss = (resids_2 ** 2).sum()
print(rss) # 0.1474209936267066
# the total sum of square (each test value's difference from the test series' mean squared)
tss = Y_2test - Y_2test.mean()
print(tss.iloc[0]**2)
# 1.4489026063100137  ## series is rounded below in one line of variable for equation
tss_2 = ((Y_2test - Y_2test.mean()) ** 2).sum()
print(tss_2) # 32.75925925925925
r_squared_manual = 1 - rss/tss_2
print(r_squared_manual, round(r_squared_manual, 2)) # 0.7569928674870116 0.76






# Split the data, initialize and fit the model
X2_train, X2_test, Y_train, Y_test = train_test_split(X2, Y, test_size=0.3, random_state=1)
model2 = LinearRegression()
model2.fit(X2_train, Y_train)

# Calculate the MAE
y_test_predicted2 = model2.predict(X2_test)
from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error(Y_test, y_test_predicted2)

# Calculate the R-squared
from sklearn.metrics import r2_score
r_squared = r2_score(Y_test, y_test_predicted2)

# Print results
print(model2.intercept_.round(2) , MAE.round(2) , r_squared.round(2))

## 2.06 0.31 0.77





















 