import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('D:/Hassan/7th sem assessment/agri/crop_yield.csv')

# --- Optimized Plotting Functions ---

# 1. Bar Plot: Average Yield by Crop Type
def plot_avg_yield_by_crop(data):
    plt.figure(figsize=(8, 5))
    plt.bar(data['Crop'].unique(), data.groupby('Crop')['Yield_tons_per_hectare'].mean(), color="skyblue")
    plt.title("Average Yield by Crop Type")
    plt.xlabel("Crop")
    plt.ylabel("Yield (tons/hectare)")
    plt.savefig("average_yield_by_crop.png")
    plt.close()  # Close the plot to free memory

# 2. Line Plot: Yield over Temperature Ranges
def plot_yield_by_temperature(data):
    data_sorted_temp = data.sort_values(by='Temperature_Celsius')
    plt.figure(figsize=(8, 5))
    plt.plot(data_sorted_temp['Temperature_Celsius'], data_sorted_temp['Yield_tons_per_hectare'], 
             color='blue', marker='o', linestyle='-')
    plt.title("Yield Across Temperature Ranges")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Yield (tons/hectare)")
    plt.savefig("yield_by_temperature.png")
    plt.close()

# 3. Scatter Plot: Yield vs Rainfall
def plot_yield_vs_rainfall(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data['Rainfall_mm'], data['Yield_tons_per_hectare'], color='purple', alpha=0.6)
    plt.title("Yield vs Rainfall")
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("Yield (tons/hectare)")
    plt.grid(True)
    plt.savefig("yield_vs_rainfall.png")
    plt.close()

# 4. Pie Chart: Fertilizer Usage Distribution
def plot_fertilizer_usage(data):
    fertilizer_counts = data['Fertilizer_Used'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(fertilizer_counts, labels=['Fertilizer Used', 'No Fertilizer'], autopct='%1.1f%%', startangle=140, 
            colors=['#66c2a5', '#fc8d62'])
    plt.title("Fertilizer Usage Proportion")
    plt.savefig("fertilizer_usage.png")
    plt.close()

# 5. Stacked Bar Chart: Irrigation Use by Soil Type
def plot_irrigation_by_soil(data):
    irrigation_soil = data.groupby(['Soil_Type', 'Irrigation_Used']).size().unstack()
    irrigation_soil.plot(kind='bar', stacked=True, figsize=(8, 5), color=['#8da0cb', '#e78ac3'])
    plt.title("Irrigation Use Across Soil Types")
    plt.xlabel("Soil Type")
    plt.ylabel("Count")
    plt.legend(title="Irrigation Used")
    plt.savefig("irrigation_by_soil.png")
    plt.close()

# 6. Box Plot: Yield under Weather Conditions
def plot_yield_by_weather(data):
    plt.figure(figsize=(8, 5))
    data.boxplot(column='Yield_tons_per_hectare', by='Weather_Condition', grid=False)
    plt.title("Yield Distribution under Weather Conditions")
    plt.suptitle("")  # Remove the automatic title from boxplot
    plt.xlabel("Weather Condition")
    plt.ylabel("Yield (tons/hectare)")
    plt.savefig("yield_by_weather.png")
    plt.close()

# Call each function to save the plots
plot_avg_yield_by_crop(data)
plot_yield_by_temperature(data)
plot_yield_vs_rainfall(data)
plot_fertilizer_usage(data)
plot_irrigation_by_soil(data)
plot_yield_by_weather(data)
