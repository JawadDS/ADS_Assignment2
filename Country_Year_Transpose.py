# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023

@author: Jay

The below code is the answer for question 1 in the assignment. In this code,
I have created a function that takes a file and returns two DataFrames, 
one with countries as columns and one with years as columns.

The data has been retrieved from the World Bank website.
Link: https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv
The data was too large, so I selected data for 9 countries for 4 years and saved it in a file ('Access_to_Electricity').
I have uploaded that file to my GitHub repository, so to run this code, you need to use the file from my GitHub repository.
Link: https://github.com/JawadDS/ADS_Assignment2/blob/main/Access_to_Electricity.csv

"""

import pandas as pd
import numpy as np

def read_data_function(data_file):
    """
    Reads a CSV file containing data on access to electricity.

    Parameters:
        data_file (str): The path to the CSV file.

    Returns:
        df_countries (DataFrame): Original DataFrame with countries as rows.
        df_years (DataFrame): Transposed DataFrame with years as rows.
    """
    # Read the CSV file into a DataFrame, using the first column as the index
    df_countries = pd.read_csv(data_file, index_col = 0)
    
    # Transpose the DataFrame to have years as rows
    df_years = df_countries.transpose()
    
    # Rename the index to 'Year'
    df_years = df_years.rename_axis('Year', axis = 1)
    
    return df_countries, df_years

def skew(df_countries):
    """ Calculates the centralized and normalized skewness of distribution. """
    
    # calculates average and std, dev for centralizing and normalizing
    aver = np.mean(df_countries)
    std = np.std(df_countries)
    
    # now calculate the skewness
    value = np.sum(((df_countries - aver) / std)**3) / len(df_countries - 2)
    
    return value

def kurtosis(df_countries):
    """ Calculates the centralized and normalized excess kurtosis of distribution. """
    
    # calculates average and std, dev for centralizing and normalizing
    aver = np.mean(df_countries)
    std = np.std(df_countries)
    
    # now calculate the kurtosis
    value = np.sum(((df_countries - aver) / std)**4) / len(df_countries - 3) - 3.0
    
    return value


# Calling the function and saving the returned DataFrames
df_countries, df_years = read_data_function('Access_to_Electricity(Rural).csv')

# Display the original DataFrame with countries as rows
print("DataFrame with Countries as Rows:")
print(df_countries)

# Display the transposed DataFrame with years as rows
print("\nDataFrame with Years as Rows:")
print(df_years)

# Additional statistical calculations
print("Skewness:")
print(skew(df_countries))

print("\nKurtosis:")
print(kurtosis(df_countries))

print("\nDescriptive Statistics:")
print(df_countries.describe())

print("\nCumulative Sum:")
print(df_countries.cumsum())

print("\nCumulative Product:")
print(df_countries.cumprod())
