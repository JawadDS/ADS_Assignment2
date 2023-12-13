# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023
@author: Jay

The below code produces a bar plot of Energy Use(kg of oil equivalent per capita) data for 9 countries
for the period of 2011 to 2014.

The data has been obtained from the World Bank website: 
https://data.worldbank.org/indicator/EG.USE.PCAP.KG.OE
As the original dataset was too large, a subset containing information for 9 countries over 4 years 
was saved to a file ('Access_to_Electricity.csv'). To run this code, use the file from my GitHub repository.
Link: https://github.com/JawadDS/ADS_Assignment2/blob/main/Energy_Use.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_energy_data(file_path):
    """
    Reads energy use data from a CSV file into a pandas DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df

def plot_energy_use(df):
    """
    Plots energy use by country over the years as a line plot.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    """
    # Set 'Country' column as the index
    df.set_index('Country', inplace = True)

    # Plot the data as a line plot
    plt.figure(figsize = (12, 8))

    for country in df.index:
        plt.plot(df.columns, df.loc[country], label = country)

    plt.title('Energy Use Over Years by Country')
    plt.xlabel('Year')
    plt.ylabel('Energy Use(kg of oil equivalent per capita)')
    plt.legend(title = 'Country', bbox_to_anchor=(1.05, 1), loc = 'upper left')
    plt.grid(True)
    plt.show()
# Read the energy use data using the function
energy_data_df = read_energy_data('Energy_Use.csv')

# Plot the energy use using the function
plot_energy_use(energy_data_df)
