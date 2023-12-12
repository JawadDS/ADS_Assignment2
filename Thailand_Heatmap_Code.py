# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:48:48 2023

@author: Jay
This code produces a correlation heatmap for Thailand using data obtained from the World Bank website.
The data has been cleaned, stored in a data file, and uploaded to a GitHub repository.
To run this program, download the data file from the my GitHub repository using the provided link below:

GitHub Repository: https://github.com/JawadDS/ADS_Assignment2/blob/main/Thailand_Heatmap_data.csv

"""

#import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_and_plot_heatmap(file_path):
    """
    Read data from a CSV file and plot a correlation heatmap.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - None
    """
    # Read data from the CSV file
    df = pd.read_csv(file_path)

    # Calculate the correlation matrix
    correlation_matrix = df.corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Correlation Heatmap For Thailand (2010-2014)')
    plt.show()

# Calling the function and passing data file
read_and_plot_heatmap('Thailand_Heatmap_Data.csv')
