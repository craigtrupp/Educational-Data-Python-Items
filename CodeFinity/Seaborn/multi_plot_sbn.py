#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:43:09 2022

@author: craigrupp
"""

# FacetGrid
# =============================================================================
# A useful approach to explore medium-dimensional data is by drawing multiple instances of the same plot on different subsets of your dataset.
# 
# FacetGrid ( aka FacetGrid()) object takes a DataFrame as input and the names of the variables that will form the row, column, or hue dimensions of the grid.
# 
# The variables should be categorical and the data at each level of the variable will be used for a facet along that axis.
# =============================================================================

# Importing libraries needed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df_1 = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')
print(df_1.head())
# Set the 'whitegrid' style with the 'cornsilk' facecolor
sns.set_style('whitegrid', {'axes.facecolor': 'cornsilk'})
# Create a FacetGrid variable
g = sns.FacetGrid(# Set the data
                  df,
                  # Set the col 
                  col = 'day',
                  # Set the row
                  row = 'smoker',
                  # Set the height
                  height = 3)
# Build histplots using the .map() function     
g.map(# Create histplots
        sns.histplot, 
        'total_bill',
        # Set the color
        color = 'olive', 
        # Set the kde
        kde = True, 
        # Set the fill
        fill = False,
        # Set the binwidth
        binwidth = 4)

# Display the plot
plt.show()


# PairGrid
# =============================================================================
# PairGrid ( aka PairGrid()) is a subplot grid for plotting pairwise relationships in a dataset.
# 
# This object maps each variable in a dataset onto a column and row in a grid of multiple axes. 
# Different axes-level plotting functions can be used to draw bivariate plots in the upper and lower triangles, 
# and then the marginal distribution of each variable can be shown on the diagonal.
# =============================================================================

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins_upd.csv')
# Cleaning useless columns
df = df.drop(['Unnamed: 0'], axis=1)

# Set the 'ticks' style with the 'lightpink' facecolor
sns.set_style('ticks', {'figure.facecolor' : 'lightpink'})
# Create a PairGrid variable
g = sns.PairGrid(# Set the data
                 df, 
                 # Set the hue
                 hue = 'species',
                 # Set the palette
                 palette = 'rocket_r', 
                 # Setting the diag_sharey
                 diag_sharey = False)
# Set diagonale plots using the .map_diag() function
g.map_diag(# Create a histplot
           sns.histplot,
           # Set the kde
           kde = True)
# Set non-diagonale plots using the .map_offdiag() function
g.map_offdiag(# Create a scatterplot
              sns.scatterplot,
              # Set the linewidth
              linewidth = 0.9,
              # Set the edgecolor
              edgecolor = 'purple')

# Adding the legend
g.add_legend()
# Displaying the plot
plt.show()

print(df.head())
print(df.columns)



# JointGrid
# =============================================================================
# The JointGrid ( aka JointGrid()) is a figure-level function, when the function is called a JointGrid() object is instantiated. 
# The function creates a JointGrid object consisting of three axes objects but does not plot anything on it.
# =============================================================================


















