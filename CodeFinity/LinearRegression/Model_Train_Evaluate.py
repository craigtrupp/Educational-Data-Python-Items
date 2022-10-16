#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:37:20 2022

@author: craigrupp
"""

## Train-Split Evaluation
# =============================================================================
# How to build a model to predict future values? In this section, we will work with sklearn to develop and train our model. 
# First, import LinearRegression() to create the linear regression class (model now intialized)
# =============================================================================
        
## Train - Test
# =============================================================================
# Second, we have to split the data. 
# We will use the train-test split technique for evaluating the method of a machine learning algorithm. Split the data into 2 categories:
# 
# Train Dataset: Used to train our model.
# Test Dataset: Used to evaluate the fitted model.
# =============================================================================

## Sets Defined 
# =============================================================================
# The first set is used to find the model, while the second subset is used for predictions and comparison with expected values. 
# Although, when you have a small dataset, this procedure shouldn't be used.
# 
# There is no optimal rule for the split percentage, it depends on goals, computational costs, set representativeness, and other factors, 
# but it’s good to split data 70-30 (70% of data for training and 30% - for testing).
# 
# 
# We will work in this section with train_test_split() function. 
# It takes the dataset (x and y), the size of the test/train data, and returns it as output 2 subsets:
# =============================================================================

## Random State
# =============================================================================
# The rows are randomly assigned to sets. This happens so that the datasets are representative samples (e.g., a random sample) of the original data set. 
# When comparing algorithms, it is sometimes important that they fit and evaluate on the same subsets. 
# To do this, it is desirable to fix the initial value for the pseudo-random number generator using the function parameter random_state for the above-described method
# =============================================================================

### Split Wine Dataset

# Import the libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_wine

# Load the dataset
wine = load_wine()

# Configure pandas to show all features
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# Define the DataFrame
data = pd.DataFrame(data = wine['data'], columns = wine['feature_names'])

# Define the target 
# wine.target is just an attribute name for the load_wine class that we imported from sklearn.datasets. 
# This attribute gives the values of the dataset we are trying to predict.
data['flavanoids'] = wine.target

# Define the data we will work with
x = data[['total_phenols']]
y = data['flavanoids']

# Build and fit the model : Split the data 60-40 (60% of the data is for training and 40% is for testing
model = LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.4, random_state = 1)

# Print results
print(Y_train)


### Fitting
# =============================================================================
# Fitting the model means finding the most appropriate model based on training data
# 
# model.fit(X_train,Y_train)
# 
# This method executes computations storing the result in the model object. 
# So, our model has been built, and we have parameters for our straight line. 
# Let’s take a look at the intercept and slope we have received.
# =============================================================================

## Linear Regression model properties (All model parameters in sklearn have trailing underscores.)
model.fit(X_train, Y_train)
print(model.intercept_)
print(model.coef_)

## Model parameters (Intercept & Slope) for model with a 60% train size
## Having these two parameters, we can build the line to predict future values on our dataset
# =============================================================================
# -1.2679266384148526
# [1.42740605]
# =============================================================================

## Different Random State
# Build and fit the model
model_1 = LinearRegression()
X_train_1, X_test_1, Y_train_1, Y_test_1 = train_test_split(x, y, test_size=0.4, random_state=1)
model_1.fit(X_train, Y_train)

# Print parameters
print(model_1.intercept_)
print(model_1.coef_)

## Coefficients (Intercept & Slope)
# =============================================================================
# 2.877520542132497
# [-0.84090581]
# =============================================================================


## Prediction - .predict()
#Once we've trained our module, it's time to think about test data evaluation and future predictions

import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.4, random_state = 1)
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
new_total_phenols = np.array([2]).reshape(-1, 1)
predicted_value = model.predict(new_total_phenols)
print(predicted_value) # [1.19570893]



## Task
# =============================================================================
# In this task, you build, train and fit your model and make predictions based on it. 
# This time you will make predictions about total_phenols, based on flavanoids. It means that your target now is total_phenols
# =============================================================================
# Define the target
data['total_phenols'] = wine.target

# Define the data we will work with
x = data[['flavanoids']]
y = data['total_phenols']

# Build and fit the model
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
new_flavanoids = np.array([1]).reshape(-1, 1)
predicted_value = model.predict(new_flavanoids)
print(predicted_value) # [1.59896631]



## Residual or error - Residuals
# =============================================================================
# We can measure the distance between a point and a line along the y-axis. This distance is called the residual or error. 
# The remainder is the difference between the observed value of the target and the predicted value. The closer the residual is to 0, 
# the better our model performs. Let's calculate the residuals and present them as a chart.
# =============================================================================
# =============================================================================
# Ideally, the remains should be arranged symmetrically and randomly around the horizontal axis. 
# Still, if the residual graph shows some pattern (linear or non-linear), it means that our model is not the best.
# =============================================================================
# Work with residuals
y_test_predicted = model.predict(X_test)
# Assign the difference between variables
residuals = Y_test - y_test_predicted
print(residuals)

## Sample of Residuals (Not Absolute Residuals))
# =============================================================================
# 161    0.121003
# 117    0.094747
# 19    -0.307006
# 69    -0.420765
# =============================================================================
print(type(residuals), len(residuals), len(data['flavanoids']), len(X_test)) # <class 'pandas.core.series.Series'> 54 178 54
# Let's take a quick look at our residual values (just interested in series values not their row value)
print(residuals[0:5].values, '\n', Y_test[0:5].values, '\n', y_test_predicted[0:5])
## Y_test values
# [2 1 0 1 0]

## y_test_predicted values 
# [1.87899718 0.90525349 0.30700573 1.42076485 0.45974983]
print((Y_test.iloc[0] - y_test_predicted[0]) == residuals.iloc[0]) # True



## Mean Absolute Error - MAE (Sum of Residuals / len(objects))
# =============================================================================
# Residuals plot is a good way to see if our model is good but not the best. 
# Let's look at the metrics that are commonly used to evaluate a regression model
# 
# Large dataset/set of residuals 
# Analyzing each of the tens of thousands of residues is quite a marginal business. 
# Therefore, in this case it is easier to take the sum of residuals and divide it by the number of objects in our sample
# 
# Moreover, if we get a very small value that is close to zero, this does not mean that our model is good, it can happen when the positive 
# and negative residuals themselves are reduced to a very small number
# 
# Thus, it becomes evident that taking the deviation of predictions from the truth and averaging is not 
# the best calculation metric performance of our model. We need to come up with something more complex. 
# First, we require to get rid of the minus sign. This can be done using the module, that is, 
# take the sum of the modules of the differences (thereby, our negative deviation becomes positive and 
# there will no longer be such that the negative and positive deviation add up to zero) and divide by the number of objects, 
# thereby obtaining the mean absolute error (MAE).
# 
# Abs value will be best for any observed residual difference so negative/positive residual errors don't give the illusion of close to zero or a good model fit

# MAE = abs(residuals).mean()

# We can also use the method mean_squared_error() from scikit-learn metrics module to output the same result
# from sklearn.metrics import mean_absolute_error
# print(mean_absolute_error(Y_test, y_test_predicted))
# =============================================================================

print(residuals.iloc[0:5])
## 
# =============================================================================
# 161    0.121003
# 117    0.094747
# 19    -0.307006
# 69    -0.420765
# 53    -0.459750
# =============================================================================
print(abs(residuals.iloc[0:5]))
# =============================================================================
# 161    0.121003
# 117    0.094747
# 19     0.307006
# 69     0.420765
# 53     0.459750
# =============================================================================


# Calculate the MAE mathematically - we need to get the absolute value (aka positive value before getting the mean)
MAE_math = abs(residuals).mean()
print(MAE_math) # 0.3072487659097363
# Calculate the MAE using built function
from sklearn.metrics import mean_absolute_error
## Actual Test Set Values, Predicted Values from model for method argument order
MAE_func = mean_absolute_error(Y_test, y_test_predicted)
print(MAE_func) # 0.3072487659097363

# Print results
print(MAE_math == MAE_func) # True


## MSE and RMSE

## MSE - Mean Square Error
# =============================================================================
# We could square our differences, that is, we take our predictions, subtract the true values ​​from them and square them, 
# thereby obtaining the squared deviation. Now we can sum all the squared deviations and divide by their number of objects. 
# This value shows how much our predictions deviate from the truth squared. It is called the mean square error or MSE. 
# When the MSE goes to zero, in this case, all true values ​​match our predictions perfectly.

## However (Our MSE Units will no longer match our target value (y-axis)) .. enter RMSE
# =============================================================================

## RMSE - Root Mean Squared Error
# =============================================================================
# It is important to note that when calculating the error, the MSE units do not match the original units of the predicted target value. 
# We predict the number of phenols squared, which is sometimes a bit difficult to use for estimation. You can get rid of this square quite 
# simply by taking the square root of MSE. It calls the root mean squared error (RMSE). Thus, it may be common to use the MSE loss 
# to train a regression prediction model and use the RMSE to evaluate and report its performance.
# =============================================================================

## Note - On all Metrics
## Ideally, all the metrics that we considered (MSE, RMSE, MAE) tend to zero when all true values are very close to predictions.

# Calculate MSE and RMSE
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(Y_test, y_test_predicted)
print(MSE)

import math 
#RMSE = math.sqrt((residuals ** 2).mean())
RMSE = math.sqrt(MSE)
print(RMSE)

## MSE & RMSE
# =============================================================================
# 0.1396695763431366 - MSE
# 0.3737239306535462 - RMSE
# =============================================================================


# R-squared (Coefficient of Determination)
# =============================================================================
# This metric is R-squared or is also called the coefficient of determination. 
# It is used to test how well the observed results are reproduced by the model. 
# 
# Equation : R^2 = 1 - RSS/TSS
# RSS = the sum of squares of residuals
# TSS = the total sum of square  ... which is the target's test return value (from train_test_split) minus it's own mean, each value squared and finally the sum
# 
# RSS = (residuals**2).sum()
# TSS = ((Y_test - Y_test.mean())**2).sum()
# r2 = 1 -RSS/TSS
# =============================================================================

RSS = (residuals**2).sum()
TSS = ((Y_test - Y_test.mean())**2).sum()
r2 = 1 -RSS/TSS
print(r2) # 0.7697702178538235

## Coefficient Value Gauge
# =============================================================================
# The best possible estimate for the coefficient of determination is 1, which is obtained when the predicted values coincide with the actual values, 
# that is, the residuals are zero and, accordingly, RSS. If R-squared is 0, it means that the model does not explain any of the variations in the response
# variable around its mean. It happens that R-squared becomes negative, you should not be afraid. This happens when we have a prediction that is not 
# the most successful, that is, the model did not learn very well. When we subtract the truth from these predictions, we will get large deviations and, 
# as a result, a large negative value at the end when subtracting from 1.

## The higher the R-squared, the better the model fits our data.
# =============================================================================

## We can get R-squared using the .score() method:
# Calculate R-squared w/Test returns from train_test_split
r_squared_model = model.score(X_test, Y_test) 
print(r_squared_model)

from sklearn.metrics import r2_score
r_squared_model_func = r2_score(Y_test, y_test_predicted)
print(r_squared_model_func)

## Matches output for equation above and plugging in existing variables
# =============================================================================
# 0.7697702178538235
# 0.7697702178538235
# =============================================================================


## Not Always the Linear Regression?
# =============================================================================
# In 1973, the English mathematician Francis Anscombe, to illustrate the importance of using graphs for statistical analysis, 
# and the impact of outliers on the properties of the entire data set, composed 4 datasets (it also called Anscombe's quartet). 
# The simple statistical properties of these sets are identical. 
# They have the same mean for each variable, variance, the correlation between x and y, linear regression line, and even R-squared. 
# However, their graphs differ significantly. Each set consists of 11 pairs of numbers.
# =============================================================================
import seaborn as sns
from scipy.stats import stats

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


# Find linear regression parameters
def regression(x, y):
   slope, intercept, r, p, std_err = stats.linregress(x,y)
   print(f'slope = {slope.round(2)}  intercept = {intercept.round(2)}  r = {r.round(2)}')
   sns.regplot(x, y)

# Apply the function to all datasets
regression(x1, y1)
regression(x2, y2)
regression(x3, y3)
regression(x4, y4)

## Same Returns ... For Varying Visuals
# =============================================================================
# slope = 0.5000909090909091  intercept = 3.0000909090909103  r = 0.8164205163448399
# slope = 0.5000000000000001  intercept = 3.000909090909089  r = 0.816236506000243
# slope = 0.4997272727272729  intercept = 3.002454545454544  r = 0.8162867394895984
# slope = 0.4999090909090909  intercept = 3.0017272727272726  r = 0.8165214368885028
# =============================================================================




