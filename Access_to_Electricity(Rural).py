# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:21:46 2023

@author: Jay

The below code read a csv file and explore some different statistical tools such as describe, groupby, transpose, cumsum and prodsum.

The data has been taken from the world bank website 
link = https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.RU.ZS?downloadformat=csv
The Data was too large so i just took the data of 9 countries for 4 years and save it in a file ('Access_to_Electricity')
and i have upload that file to my github repositry, so in order to run this code you need use the file from my github ripostry.
Link = https://github.com/JawadDS/ADS_Assignment2/blob/main/Access_to_Electricity(Rural).csv

"""

import pandas as pd

# Load the data from the CSV file
file_path = 'Access_to_Electricity(Rural).csv'

# Read CSV data into a pandas DataFrame with 'Country' as the index
electricity_data = pd.read_csv(file_path, index_col=0)

# Transpose the DataFrame to have 'Year' as the column index
transposed_data = electricity_data.transpose()

# Rename the axis to 'Year'
transposed_data = transposed_data.rename_axis('Year', axis=1)

# Group by 'Country'
grouped_data = transposed_data.groupby(level=0)

# Calculate cumulative sum and product for each country across the years
cumulative_sum_data = electricity_data.cumsum()
cumulative_product_data = electricity_data.cumprod()

# Display descriptive statistics for the original data
print("Descriptive Statistics:")
print(electricity_data.describe())

# Display cumulative sum data
print("\nCumulative Sum:")
print(cumulative_sum_data)

# Display cumulative product data
print("\nCumulative Product:")
print(cumulative_product_data)

# Display transposed data
print("\nTransposed Data:")
print(transposed_data)
