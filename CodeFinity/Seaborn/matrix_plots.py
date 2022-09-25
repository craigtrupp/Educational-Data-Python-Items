#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:29:25 2022

@author: craigrupp
"""

# =============================================================================
# Heat Map
# A heatmap (aka heatmap()) is a plot of rectangular data as a color-encoded matrix. As parameter, it takes a 2D dataset. 
# That dataset can be coerced into an ndarray.

# This is a great way to visualize data because it can show the relation between variabels including time. For instance, the number of fligths through the years.
# =============================================================================

# Importing libraries needed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/flights.csv')
# Reshaping the data
upd_df = df.pivot('month', 'year', 'passengers')
print(upd_df)

# Set the 'ticks' style with the 'seagreen' figure facecolor
sns.set_style('ticks', {'figure.facecolor' : 'seagreen'})
# Create a heatmap
sns.heatmap(# Add the data for the heatmap
            upd_df,
            # Set the cmap
            cmap = 'viridis',
            # Set the annotation
            annot = True,
            # Set the fmt
            fmt = '0.99g',
            # Set the linecolor
            linecolor = 'plum')

# Display the plot
plt.show()


# =============================================================================
# Clustermap
# A cluster map (aka clustermap()) is a matrix plot with a heatmap and two clustering dendrograms.
# =============================================================================


# Create a clustermap
sns.clustermap(# Add the data for the clustermap
               upd_df,
               # Set the cmap
               cmap = 'vlag', 
               # Set the standard_scale
               standard_scale = 1,
               # Set the method
               method = 'single',
               # Set the metric
               metric = 'correlation',
               # Set the annot
               annot = True,
               # Set the vmin
               vmin = 0,
               # Set the vmax
               vmax = 10 )

# Display the plot
plt.show()