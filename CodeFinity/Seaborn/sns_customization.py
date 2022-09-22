#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:14:29 2022

@author: craigrupp
"""

# Customize Why??
# =============================================================================
# Why customize?
# 
# personal preference
# improve readability
# guide interpretation.
# 
# Plotting in the Seaborn can be used to create 2 types of plots: FacetGrids and AxesSubplots. 
# Axes style customizations below
# =============================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fish_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/fish.csv')
print(fish_df.head())

# Create plot in variable
g = sns.histplot(x='answer', data=fish_df, binwidth=0.25)

# Set title
g.set_title('Fish')

# Show Hist
plt.show()


# Labels & Ticks
# =============================================================================
# Setting label names:
# 
# To set label names we need to set a plot variable and use g.set(xlabel = 'x_name', ylabel = 'y_name') function, g - is the plot variable.
# 
# X(y)ticks rotation:
# 
# To rotate labels we need to use plt.xticks(rotation = n), plt.yticks(rotation = n) functions, n is the angle.
# =============================================================================

lp_df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/lineplothue.csv') 
print(lp_df.head())


g_2 = sns.lineplot(x = 'year', y = 'population', hue = 'season', data = lp_df)

g_2.set(xlabel = 'Years(2012-2022)', ylabel='Panda population')
plt.xticks(rotation=45)
plt.show()



# Style & Such
# =============================================================================
# Setting the style:
# 
# To set the style use sns.set_style('style_name') function.
# 
# Styles available in the Seaborn: white, dark, whitegrid, darkgrid, ticks.
# 
# Changing colors of the main elements of the plot:
# 
# Seaborn has different palette options. Below there are a few of them.
# 
# Palettes:
# 
# RdBu, PRGn, RdBu_r, PRGn_r - different colors in the palette
# Greys, Blues, PuRd, GnBu -  gradient colors.
# We can also create your own palette by creating a list variable. To set the palette use sns.set_palette(palette_name) function.
# 
# Context setting:
# 
# To set the context use sns.set_context('context_name') function.
# 
# Contexts available in the Seaborn: paper, notebook, talk, poster.
# =============================================================================
df_style = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/bamboo.csv')
print(df_style.head())


sns.set_style('whitegrid')

sns.set_context('paper') 

sns.countplot(x = 'Bamboo', data = df_style)

plt.xticks(rotation = 45)

plt.show()


# Let's try something a bit different
sns.set_style('whitegrid', {'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'grey', 'font.family':['monospace'], 'axes.labelcolor':'darkorange'})

sns.countplot(x = 'Bamboo', data = df_style)

plt.xticks(rotation = 45)

plt.show()



# Last Section
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/c5b4ea8f-8a30-439f-9625-ddf2effbd9ac/final_chlldg.csv')
print(df.head())
print(df['kilos'].value_counts())
# Bin our kilos measurement into bins to see how the distributions looks
colors = {'boy':'lightblue', 'girl':'pink'}
g = sns.histplot(x = 'kilos', hue = 'gender', palette = colors, data = df, binwidth = 0.1, bins=15)
g.set_title('Yummy fish!', color = 'white')
g.set(xlabel = 'Kilos of fish')
sns.set_context('paper')
sns.set_style('darkgrid', {'axes.facecolor':'white', 'figure.facecolor':'black', 'axes.labelcolor':'white', 'xtick.color':'white', 'ytick.color':'white'})
plt.show()



