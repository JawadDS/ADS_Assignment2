# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas dataframe
data = pd.read_csv('Access_to_Electricity.csv')

# Set 'Country' as the index for better visualization
data.set_index('Country', inplace=True)

# Create a bar plot for the data with transparency (alpha) for better readability
plt.figure(figsize=(12, 8))
data.plot(kind='bar', alpha=0.7)

# Setting labels and title for better understanding
plt.xlabel('Countries')
plt.ylabel('% of Population')
plt.title('Access to Electricity from 2018 to 2021')

# Place the legend outside the plot area for better visibility
plt.legend(title='Years' ,  loc='upper left', bbox_to_anchor=(1, 1))

# Set the y-axis range from 0 to 100 for a percentage scale
plt.ylim(0, 100)

# Display the plot
plt.show()
