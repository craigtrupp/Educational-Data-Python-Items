#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:38:53 2022

@author: craigrupp
"""

# Regplot
# =============================================================================
# The regplot ( aka regplot()) is used to plot data and a linear regression model fit. 
# There are a number of mutually exclusive options for estimating the regression model.
# =============================================================================

# Importing libraries needed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')

# Set the 'darkgrid' style with the 'tan' figure facecolor and 'cornsilk' axes facecolor
sns.set_style('darkgrid', 
              {'figure.facecolor' : 'tan', 
              'axes.facecolor' : 'cornsilk'})

# Create a regplot
sns.regplot(# Set the x
            x = 'total_bill', 
            # Set the y
            y = 'tip', 
            # Set the marker
            marker = '+',
            # Set the color
            color = 'green',
            # Disable the fit_reg
            fit_reg = True,
            # Set the data
            data = df)

# Display the data       
plt.show()


# lmplot
# =============================================================================
# The lmplot ( aka lmplot()) combines regplot() and FacetGrid. 
# It is intended as a convenient interface to fit regression models across conditional subsets of a dataset.
# =============================================================================

# Set the 'darkgrid' style with the 'lightpink' figure facecolor
sns.set_style('darkgrid', {'figure.facecolor' : 'lightpink'})
# Create a lmplot
sns.lmplot(# Set the x
           x = 'total_bill', 
           # Set the y
           y = 'tip', 
           # Set the hue
           hue = 'smoker', 
           # Set the col
           col = 'sex',
           # Set the markers
           markers = ['o', 'x'],
           # Set facet_kws 
           facet_kws = {'legend_out' : True},
           # Set the palette
           palette = 'crest',
           # Set the data
           data = df)

# Display the plot         
plt.show()
