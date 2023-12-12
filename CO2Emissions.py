# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023
@author: Jay

The below code produces a bar plot of CO2 Emissions data for 9 countries
for the period of 2011 to 2014.

The data has been obtained from the World Bank website: 
https://data.worldbank.org/indicator/EN.ATM.CO2E.KT
As the original dataset was too large, a subset containing information for 9 countries over 4 years 
was saved to a file ('Access_to_Electricity.csv'). To run this code, use the file from my GitHub repository.
Link: https://github.com/JawadDS/ADS_Assignment2/blob/main/CO2Emissions.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    """
    Reads data from a CSV file into a pandas DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df

def plot_co2_emissions(df):
    """
    Plots CO2 emissions by country over the years as a bar plot.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    """
    # Set 'Country' column as the index
    df.set_index('Country', inplace=True)

    # Plot the data as a bar plot
    df.plot(kind='bar')

    plt.title('CO2 Emissions by Country (2011-2020)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emission (in million metric tons)')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

 # Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
file_path = 'CO2Emissions.csv'

# Read the data using the function
data_df = read_data(file_path)

# Plot the CO2 emissions using the function
plot_co2_emissions(data_df)
