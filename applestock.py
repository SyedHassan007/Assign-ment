import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Apple stock data
data = pd.read_csv('D:/Hassan/7th sem assessment/aapldata/AAPL.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())
# Using the 'Close' column for analysis
close_prices = data['Close']

# Mean
mean_price = np.mean(close_prices)
print(f"Mean Close Price: {mean_price}")

# Median
median_price = np.median(close_prices)
print(f"Median Close Price: {median_price}")

# Mode (using Pandas mode method)
mode_price = close_prices.mode().values[0]
print(f"Mode Close Price: {mode_price}")

# Standard Deviation
std_dev_price = np.std(close_prices)
print(f"Standard Deviation of Close Price: {std_dev_price}")
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], close_prices, label='Close Price', color='blue')
plt.axhline(mean_price, color='red', linestyle='--', label=f'Mean: {mean_price:.2f}')
plt.axhline(median_price, color='green', linestyle='--', label=f'Median: {median_price:.2f}')
plt.title('Apple Stock Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
