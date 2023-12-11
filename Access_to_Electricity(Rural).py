# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:21:46 2023
@author: Jay

The below code reads a CSV file and explores various statistical tools such as describe, groupby, transpose, cumsum, and cumprod.

The data has been extracted from the World Bank website using the following link:
https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.RU.ZS?downloadformat=csv

Due to the large size of the data, a subset containing information for 9 countries over 4 years has been saved to a file ('Access_to_Electricity').
This file is hosted on my GitHub repository, and to run this code, you can access it from the following link:
https://github.com/JawadDS/ADS_Assignment2/blob/main/Access_to_Electricity(Rural).csv
"""

import pandas as pd

def read_data_function(filename):
    """
    Reads the data from a CSV file into a pandas DataFrame.

    Parameters:
    - filename (str): The path to the CSV file.

    Returns:
    - data (DataFrame): The loaded data.
    """
    # Read the data from the CSV file into a pandas dataframe
    data = pd.read_csv(filename, index_col=0)
    return data

# Read CSV data into a pandas DataFrame with 'Country' as the index
electricity_data = read_data_function('Access_to_Electricity(Rural).csv')
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
