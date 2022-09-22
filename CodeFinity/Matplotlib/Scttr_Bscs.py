#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:28:02 2022

@author: craigrupp
"""

# Scatter Plots - Intro
# =============================================================================
# Let's consider one more plot type widely used in analytics - scatter plots. 
# This type of plot is quite easy to understand - it's just a collection of points having specific coordinates. 
# Often this type of plot is used in experiments or discovering if there is relation between factors.
# =============================================================================


# Build - Define
# =============================================================================
# To build a scatter plot we need to do the same as for a simple line plot. 
# But this time we use .scatter() applied to Axes object (instead of .plot() in the previous section). 
# The first parameter of this function will be the x-axis, and the second - y-axis.
# =============================================================================


# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/ed80401e-2684-4bc4-a077-99d13a386ac7/gapminder2017.csv', index_col=0)
print(data.head())
print(data.columns)

# Create Figure and Axes objects
fig, ax = plt.subplots()

# Initialize the scatter plot
ax.scatter(data["gdp per capita"], data["life exp"])

# Display the plot
plt.show()



# Set parameters
# =============================================================================
# To set the chart limits we use .set() function applied to Axes object (usually named ax). This function has the following parameters (but not only):
# 
# xlim, ylim - tuple with minimum and maximum value to be displayed on x or y-axis respectively;
# xticks, yticks - list/array with ticks to be displayed on x or y-axis respectively;
# xlabel, ylabel - string with the text to be displayed on x or y-axis respectively;
# title - string to be displayed as the plot title.
# =============================================================================
import numpy as np

# New fig,ax instance
fig_2, ax_2 = plt.subplots()

ax_2.scatter(data['gdp per capita'], data['life exp'])

# GDP xticks (range)
print(data['gdp per capita'].max(), data['gdp per capita'].min())

# np.arange(start, end, step)
ax_2.set(xlim = (0, 30000), ylim = (45, 90), xticks = np.arange(data['gdp per capita'].min() - 500, data['gdp per capita'].max() + 500, 10000))
ax_2.set_xticklabels(np.arange(data['gdp per capita'].min() - 500, data['gdp per capita'].max() + 500, 10000), rotation=45)

plt.show()




# =============================================================================
# Color & Size
# To set the points color use parameter c (possible values for this parameter are the same as for color parameter in .plot() function from the previous section), 
# to set the size of the points use s parameter (either single integer/float number or array with the same size as the number of points)
# =============================================================================

# Create Figure and Axes objects
fig_3, ax_3 = plt.subplots()

# Initialize the scatter plot
ax_3.scatter(data["gdp per capita"], data["life exp"], c = 'darkorange', s = 1.5)

# Display the plot
plt.show()



# Grouping Observations
# =============================================================================
# One more common usage of scatter plots is cluster analysis - 
# finding if there is some relation between groups of observations and if we can statistically divide the observations into groups.
# =============================================================================

# Fig subplots
fig_4, ax_4 = plt.subplots()

# Inique colors for number of unique regions to scatter
colors = ["r", "g", "b", "c", "m"]
regions = data.continent.unique()

# Loop through length of color, set index to unique region's boolean series return (True/False) - telling scatter what to plot
# Assign unique colors[i] and regions[i] to color and label property
for i in range(len(colors)):
    print(i, colors[i], regions[i])
    # set bool_index series
    idxs = data['continent'] == regions[i]
    # Scatter continet's found row instances through chaining the series to the dataframe and then selecting axis column
    ax_4.scatter(data[idxs]['gdp per capita'], data[idxs]['life exp'], c = colors[i], label = regions[i])

# Show Legend
plt.legend()
# Show Continent Scatter group
plt.show()
    



# Grouping Further Observations (Numeric) - Colormap
# =============================================================================
# In the previous chapter, we colored the points in accordance with the continent. 
# This was the categorical variable (which means it can take on one of a limited, usually fixed, number of possible values). 
# But what if we want to use colors in accordance with a numeric variable? 
# In that case, most likely, we are talking about the continuous variable (can take on an uncountable set of values). 
# A popular solution is using colormaps (I assume you heard about heatmaps).
# =============================================================================

# Create Figure and Axes objects
fig_5, ax_5 = plt.subplots()

print(data['hdi'].value_counts())

# Initalizing the plot
cax = ax_5.scatter(data["gdp per capita"], data["life exp"], c = data["hdi"], cmap = 'plasma')

# Display the legend for colormap
fig_5.colorbar(cax)

# Display the plot
plt.show()


# =============================================================================
# # Make Chart More Informative
# =============================================================================

# Create Figure and Axes objects
fig, ax = plt.subplots()

# Initalizing the plot
cax = ax.scatter(data["gdp per capita"], data["life exp"], c = data["hdi"], cmap = 'plasma')

# Add labels and title
ax.set(xlabel = 'GDP per capita', ylabel = 'Life expectancy', title = 'GDP per capita and life expectancy')

# Display the legend for colormap
cbar = fig.colorbar(cax)
cbar.ax.set_title("HDI", fontsize=10)
# Below isn't working so just setting the cbar title I guess
cbar.ax.set_xlabel("HDI", fontsize=10)

# Display the plot
plt.show()

