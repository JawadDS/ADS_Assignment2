# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023
@author: Jay

The below code produces a bar plot of Electric Power Consumption data for 9 countries
for the period of 2011 to 2014.

The data has been obtained from the World Bank website: 
https://data.worldbank.org/indicator/EG.USE.ELEC.KH.PC 
As the original dataset was too large, a subset containing information for 9 countries over 4 years 
was saved to a file ('Electric_Power_Consumption.csv'). To run this code, use the file from my GitHub repository.
Link: https://github.com/JawadDS/ADS_Assignment2/blob/main/Electric_Power_Consumption.csv
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

def read_data_function(filename):
    """
    Reads the data from a CSV file into a pandas DataFrame.

    Parameters:
    - filename (str): The path to the CSV file.

    Returns:
    - data (DataFrame): The loaded data.
    """
    # Read the data from the CSV file into a pandas dataframe
    data = pd.read_csv(filename)
    return data

# Read CSV data into a pandas DataFrame
data = read_data_function('Electric_Power_Consumption.csv')

# Set 'Country' as the index for better visualization
data.set_index('Country', inplace = True)

# Create a bar plot for the data with transparency (alpha) for better readability
plt.figure(figsize = (12, 8))
data.plot(kind='bar', alpha = 0.7)

# Setting labels and title for better understanding
plt.xlabel('Countries')
plt.ylabel('kWh')
plt.title('Electric Power Consumption (kWh per capita)')

# Place the legend outside the plot area for better visibility
plt.legend(title='Years', loc = 'upper left', bbox_to_anchor=(1, 1))

# Set the y-axis range from 0 to 5000 for better scaling
plt.ylim(0, 5000)

# Display the plot
plt.show()
