#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:09:47 2022

@author: craigrupp
"""

# Distribution
# =============================================================================
# The distributions module contains several functions designed to answer questions such as these. 
# The axes-level functions are histplot(), kdeplot(), ecdfplot(), and rugplot(). 
# They are grouped together within the figure-level displot() function.
# 
# A histogram( aka histplot()) is a classic visualization tool that represents the distribution of 
# one or more variables by counting the number of observations that fall within discrete bins.
# =============================================================================

# Importing libraries needed
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df_peng = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins.csv')
print(df_peng.head())
print(df_peng.columns)

# Create a histplot showing total density (total area = 1)
sns.histplot(# Set the x
             x = 'bill_length_mm', 
             # Set the hue
             hue = 'island',
             # Set the element : visual representation of the histogram statistic 
             element = 'step',
             # Set the stat : aggregate statistic to compute in each bin : normalize w/density such that total area of hist = 1
             stat = 'density',  
             # Set the binwidth
             binwidth = 1,
             # Set the palette
             palette = 'flare',
             # Set the data
             data = df_peng)

# Display the plot
plt.show()


# KDE
# =============================================================================
# A kernel density estimate( aka kdeplot()) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram. 
# KDE represents the data using a continuous probability density curve in one or more dimensions.
# Y-axis represents the PDE (probability density estimate) = probability per unit value of X-axis 
# It is also termed as probability differential – probability of a point occurring between two values x1 and x2, represented by the area under the curve between those two points.
# The area under the KDE plot is always 1.
# =============================================================================
df_kde = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/weather+upd.csv')
thrityfive_fortyfive = df_kde.loc[(df_kde['max_temp'] <= 45) & (df_kde['max_temp'] >= 35)]
print(len(thrityfive_fortyfive), len(df_kde), 100 * (len(thrityfive_fortyfive)/len(df_kde))) # Nearly 30% of all seen max_temps in this range 35-45 

# Setting the style
sns.set_style('ticks', {'figure.facecolor' : 'lightcyan'})
# Create a kdeplot
sns.kdeplot(# Set the x
            x='max_temp',
            # Set the hue
            hue = 'month',
            # Set the multiple
            multiple = 'stack', 
            # Disable the legend
            legend=False,
            # Add the filling
            fill = True, 
            # Set the data
            data=df_kde)

# Display the plot
plt.show()



# Rugplot
# =============================================================================
# The rugplot() is intended to complement other plots by showing the location of individual observations in an unobtrusive way.
# 
# =============================================================================
# Reading the file
df_rug = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')

# Different Sex totals
print(df_rug.groupby('sex')['total_bill'].agg(['mean', 'median']))


# Set the 'darkgrid' style 
sns.set_style('darkgrid', 
              # Disable the axes.grid
              {'axes.grid' : False, 
              # Set the 'aliceblue' facecolor
              'axes.facecolor' : 'aliceblue'})
# Create a kdeplot
sns.kdeplot(x = 'total_bill', 
            hue = 'sex', 
            palette = 'magma',
            multiple = 'layer', 
            fill = True,
            data = df_rug)

# Create a rugplot
sns.rugplot(# Set the x
            x='total_bill',
            # Set the hue 
            hue='sex', 
            # Set the height
            height = 0.05,
            # Set the palette
            palette='magma',
            # Set the data
            data = df_rug)

# Display the plot
plt.show()



# ECDF - Empirical Cumulative Density Function 
# =============================================================================
# An ECDF( aka ecdfplot()) represents the proportion or count of observations falling below each unique value in a dataset. 
# Compared to a histogram or density plot, it has the advantage that each observation is visualized directly, 
# meaning that there is no binning or smoothing parameters that need to be adjusted.
# =============================================================================

# Let's use our penguins dataset
df_peng.head()

# Cumultative density function plot : More familiar with a proportion and building up to 1 
sns.ecdfplot(# Set the x
             x='bill_length_mm', 
             # Set the hue
             hue='island',
             # Set the complementary 
             complementary = False,
             # Set the stat
             stat = 'proportion', 
             # Set the palette
             palette = 'mako',
             # Set the data
             data=df_peng)

# Count look at density function
sns.ecdfplot(# Set the x
             x='bill_length_mm', 
             # Set the hue
             hue='island',
             # Set the complementary 
             complementary = True,
             # Set the stat
             stat = 'count', 
             # Set the palette
             palette = 'mako',
             # Set the data
             data=df_peng)



# Displot - Access to Above type Distribution Charts
# =============================================================================
# The displot() provides access to several approaches for visualizing the univariate or bivariate distribution of data, 
# including subsets of data defined by semantic mapping and faceting across multiple subplots.
# 
# The kind parameter selects the approach to use: histplot(), kdeplot(), ecdfplot().
# =============================================================================

# Reading the file
df_dis = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/diamonds.csv')

# Set the 'darkgrid' style
sns.set_style('darkgrid') 
# Create a displot
sns.displot(# Set the x
            x='carat', 
            # Set the hue
            hue = 'cut', 
            # Set the col
            row = 'color',
            # Set the kind
            kind = 'kde',
            # Set the multiple 
            multiple = 'fill', 
            # Set the palette
            palette = 'viridis', 
            # Set the data
            data = df_dis)

# Displaying the plot
plt.show()





