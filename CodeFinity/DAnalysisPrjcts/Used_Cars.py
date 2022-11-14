import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/df_5', index_col=0)
print(df['Year'].describe())
# Delete 10% from the left tail and 1% from the right one
q10, q50, q99 = df['Year'].quantile(q=[0.1, 0.5, 0.99])
q10_1, q25_1, q50_1, q75_1, q99_1 = df['Year'].quantile(q = [0.1, 0.25, 0.5, 0.75, 0.99])
# Subtract the q10 from the q99
iqr = q99 - q10
iqr_norm = q75_1 - q25_1
print("The tail iqr requested values is : {}".format(iqr))
print("Our Normal IQR Range (75-25) is : {}".format(iqr_norm))
print("Min and Max Tail IQR", q10 - (1.5 * iqr), q99 + (1.5 * iqr))
print("General IQR Range Outliers", q25_1 - (1.5 * iqr), q75_1 + (1.5 * iqr))
# Apply loc[] function to the column 'Year'
df['Year'] = df['Year'].loc[(df['Year'] > q10 - 1.5*iqr) & (df['Year'] < q99 + 1.5*iqr)]

# Drop Nan values
df.dropna( inplace = True )

fig, ax = plt.subplots()
# Initialize histogram
ax.hist(df['Year'])
# Title histogram as 'Year'
plt.title('Year')

# Output histogram
plt.show()


# Your task here is to find out how much the mode and mean have changed before and after removing outliers.

# Values with outliers are mean_1 and median_1 (from the df_1), but values without outliers mean_2 and median_2 (from the df_2).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1 = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/df_5', index_col=0)
df_2 = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/df_6', index_col=0)

# Find mean value for the column 'Year' in the df_1 dataset
mean_1 = df_1['Year'].mean()
# Find mean value for the column 'Year' in the df_2 dataset
mean_2 = df_2['Year'].mean()
# Find the difference between mean values
mean_difference=((mean_1 - mean_2)/mean_2) * 100

# Find median value for the column 'Year' in the df_1 dataset
median_1 = df_1['Year'].median()
# Find median value for the column 'Year' in the df_2 dataset
median_2 = df_2['Year'].median()
# Find the difference between median values
median_difference = ((median_1 - median_2) / median_2) * 100

print("How much did the mean value change after removing outliers:")
print(mean_difference)
print("How much did the median value change after removing outliers:")
print(median_difference)

#The last task for you relates to converting. Values in the column Mileage(kms) are presented in kilometers, your task here is to follow the next algorithm:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/df_6', index_col=0)

# Convert kilometers to miles
df["Mileage(kms)"] = df['Mileage(kms)'] /  1.609344

# Rename column 'Mileage(kms)' to 'Mileage(miles)'
df.rename( columns = {"Mileage(kms)" : 'Mileage(miles)'} , inplace = True)

# Otput 5 random values of the column `Mileage(miles)`
print(df['Mileage(miles)'].sample(5))