#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:01:19 2022

@author: craigrupp
"""

# Importing libraries needed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv', index_col=0)
print(df.head(), '\n', df.index)
print(help(sns.stripplot))
# Set the 'whitegrid' style with the 'aliceblue' facecolor

# =============================================================================
# Strip plot 
# =============================================================================

sns.set_style('whitegrid', {'axes.facecolor': 'aliceblue'})
# Create a stripplot
sns.stripplot(# Set the x
              x = 'day', 
              # Set the y
              y = 'total_bill', 
              # Set the hue
              hue = 'smoker',
              # Set the size
              size = 8,
              # Set the palette
              palette = 'crest',
              # Set the marker
              marker = 'D',
              # Set the alpha
              alpha = 0.5,
              # Setting the data
              data = df)

# Displaying the plot
plt.show()


# =============================================================================
# Swarmplot
# =============================================================================
sns.set_style('whitegrid', {'axes.facecolor' : 'seashell'})
# Create a swarmplot
sns.swarmplot(# Set the x
              x = 'day', 
              # Set the y
              y = 'total_bill', 
              # Set the hue
              hue = 'sex',
              # Set the linewidth
              linewidth = 1,
              # Set the size
              size = 5,
              # Set the dodge (separates our hue into separate lines)
              dodge = True,
              # Set the palette
              palette = 'deep',
              # Setting the data
              data = df)

# Displaying the plot
plt.show()




# =============================================================================
# Boxplot - A boxplot (aka boxplot()) is a standardized way of displaying the distribution of data based on a five-number summary 
# ('minimum', first quartile (Q1), median, third quartile (Q3), and 'maximum'). 
# It can tell you about your outliers and what their values are. 
# It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed
# =============================================================================

df_planets = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/planets.csv')

# Set the 'ticks' style with the 'white' x & y ticks and 'grey' facecolor
sns.set_style('ticks', {'xtick.color' : 'white', 
                      'ytick.color' : 'white', 
                      'figure.facecolor' : 'grey'})
# Create a boxplot 
sns.boxplot(# Set the x
            x = 'distance', 
            # Set the y
            y = 'method', 
            # Setting the width
            width = 0.6,
            # Set the linewidth
            linewidth = 2,
            # Set the saturation
            saturation = 0.25,
            # Set the palette
            palette = 'vlag',
            # Setting the data
            data = df_planets)

# Displaying the plot
plt.show()


# =============================================================================
# A violin plot ( aka violinplot()) is a hybrid of a box plot and a kernel density plot, which shows peaks in the data. 
# It is used to visualize the distribution of numerical data. 
# Unlike a box plot that can only show summary statistics, violin plots depict summary statistics and the density of each variable.
# =============================================================================

# Let's use the tip's dataset
g = sns.violinplot(# Set the x
                   x = 'day',
                   # Set the y
                   y = 'total_bill', 
                   # Set the hue
                   hue = 'sex',
                   # Set the palette
                   palette = 'rocket', 
                   # Set the split / violin per hue partition
                   split = True,
                   # Set the inner
                   inner = 'point',
                   # Set the bw
                   bw = .2,
                   # Setting the data
                   data = df)

# Set the title for the plot
g.set_title('Tips violinplot')
# Displaying the plot
plt.show()


# =============================================================================
# Boxenplot
# Boxenplots ( aka boxenplot()) show the distribution differently and are better for bigger datasets. 
# Classic boxplots can have too many outliers and don't show as much information about the distribution.
# =============================================================================

# Reading the file
df_diamonds = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/diamonds.csv')

# Set the 'dark' style
sns.set_style('dark')
# Create a boxenplot using the g variable
g_box = sns.boxenplot(# Set the x
                  x = 'clarity',
                  # Set the y 
                  y = 'carat',
                  # Set the hue
                  hue = 'cut',
                  # Set the palette
                  palette = 'flare',
                  # Set the linewidth
                  linewidth = 2,
                  # Set the saturation
                  saturation = .2,
                  # Setting the data
                  data = df_diamonds)

# Set the title
g_box.set_title('Diamonds quality')
# Displaying the plot
plt.show()



# =============================================================================
# Barplot
# A bar plot ( aka barplot()) represents an estimate of the central tendency for a numeric variable 
# with the height of each rectangle and provides some indication of the uncertainty around that estimate using error bars. 
# Bar plots include 0 in the quantitative axis range, and they are a good choice when 0 is a meaningful value for the quantitative variable and you want to make comparisons against it.
# =============================================================================

# Set the 'ticks' style
sns.set_style('ticks', {'xtick.color' : 'white', 
                      'ytick.color' : 'white', 
                      'figure.facecolor' : 'grey'})
# Create a barplot
sns.barplot(# Set the x
            x = 'day', 
            # Set the y
            y = 'total_bill',
            # Set the hue
            hue = 'smoker',
            # Set the linewidth
            linewidth = 2.5, 
            # Set the capsize
            capsize = 0.1,
            # Set the errcolor
            errcolor = 'pink', 
            # Set the palette
            palette = 'magma',
            # Set the data
            data = df)

# Display the plot
plt.show()



# =============================================================================
# Pointplot
# A point plot ( aka pointplot()) represents an estimate of the central tendency for a numeric variable by the position of scatter plot points 
# and provides some indication of the uncertainty around that estimate using error bars.
# =============================================================================
sum_stats = df.groupby(['day', 'sex'])['tip'].agg(['mean', 'median','max', 'min'])
print(sum_stats)

# Let's see how this looks with the pointplot for centrality focus

# Set the 'ticks' style with the 'azure' facecolor
sns.set_style('ticks', {'axes.facecolor' : 'azure'})
# Create a pointplot using the g variable
g = sns.pointplot(# Set the x
                  x = 'day', 
                  # Set the y
                  y = 'tip',
                  # Set the hue
                  hue = 'sex',
                  # Set the markers
                  markers = ['v', 'o'],
                  # Set the palette
                  palette = 'rocket',
                  # Set the dodge
                  dodge = True,
                  # Set the capsize
                  capsize = 0.2,
                  # Set the linestyles
                  linestyles = ['-', '--'],
                  # Set the data
                  data = df)

# Setting the title
g.set_title('Tips pointplot')
# Display the plot
plt.show()






# =============================================================================
# The catplot ( aka catplot()) function provides a new framework giving access to several types of plots that show a relationship 
# between a numerical variable and one or more categorical variables, like boxplot(), stripplot() and so on. 
# Catplot can handle 8 different plots currently available in the seaborn.
# =============================================================================
# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins.csv')

# Set the 'white' style with the 'aliceblue' facecolor
sns.set_style('white', {'axes.facecolor' : 'aliceblue'})
# Create a catplot
sns.catplot(# Set the x
            x = 'species', 
            # Set the y
            y = 'body_mass_g', 
            # Set the hue
            hue = 'sex',
            # Set the row
            row = 'island',
            # Set the palette
            palette = 'viridis', 
            # Set the alpha
            alpha = 0.6,
            # Set the legend_out
            legend_out = False, 
            # Setting the data
            data = df)

# Displaying the plot   
plt.show()


















