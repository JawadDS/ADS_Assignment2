# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:53:13 2023

@author: Jay

The below code produce a bar plot of the data  Electic Power Consumption for 9 countries
for the period of 2011 to 2014.

The data has been taken from the world bank website 
link = https://data.worldbank.org/indicator/EG.USE.ELEC.KH.PC The Data was too large so i just took the data of 9 countries for 4 years and save it in a file ('Access_to_Electricity')
and i have upload that file to my github repositry, so in order to run this code you need use the file from my github ripostry.
Link = https://github.com/JawadDS/ADS_Assignment2/blob/main/Electric_Power_Consumption.csv

"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas dataframe
data = pd.read_csv('Electric_Power_Consumption.csv')

# Set 'Country' as the index for better visualization
data.set_index('Country', inplace=True)

# Create a bar plot for the data with transparency (alpha) for better readability
plt.figure(figsize=(12, 8))
data.plot(kind='bar', alpha=0.7)

# Setting labels and title for better understanding
plt.xlabel('Countries')
plt.ylabel('kWh')
plt.title('Electric power consumption (kWh per capita)')

# Place the legend outside the plot area for better visibility
plt.legend(title='Years' ,  loc='upper left', bbox_to_anchor=(1, 1))

# Set the y-axis range from 0 to 100 for a percentage scale
plt.ylim(0, 5000)

# Display the plot
plt.show()
