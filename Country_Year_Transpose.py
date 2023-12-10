# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023

@author: Jay

The below code is the answare for question 1 in the assignmnet, In this code
I have made a function which takes a file and returen 2 Dataframes one with countries as 
columns and one with years as column.

The data has been taken from the world bank website 
link = https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv
The Data was too large so i just took the data of 9 countries for 4 years and save it in a file ('Access_to_Electricity')
and i have upload that file to my github repositry, so in order to run this code you need use the file from my github ripostry.
Link = https://github.com/JawadDS/ADS_Assignment2/blob/main/Access_to_Electricity.csv



"""

import pandas as pd

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
    df_countries = pd.read_csv(data_file, index_col=0)
    
    # Transpose the DataFrame to have years as rows
    df_years = df_countries.transpose()
    
    # Rename the index to 'Year'
    df_years = df_years.rename_axis('Year', axis=1)
    
    return df_countries, df_years

# Calling the function and saving the returend DataFrames
df_countries, df_years = read_data_function('Access_to_Electricity.csv')

# Display the original DataFrame with countries as rows
print("DataFrame with Countries as Rows:")
print(df_countries)

# Display the transposed DataFrame with years as rows
print("\nDataFrame with Years as Rows:")
print(df_years)
