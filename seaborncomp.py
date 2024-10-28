import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating a sample dataset
np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Values': np.random.normal(50, 15, 100),
    'Subcategory': np.random.choice(['X', 'Y'], size=100)
})

# Set a Seaborn theme for improved aesthetics
sns.set_theme(style="darkgrid", palette="muted", font_scale=1.2)

# Plot 1: Bar plot with updated errorbar parameter
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Values', data=data, estimator=np.mean, errorbar='sd')  # errorbar instead of ci
plt.title("Average Values by Category")
plt.xlabel("Category")
plt.ylabel("Mean Value with Standard Deviation")
plt.show()

# Set a different theme for the next plot
sns.set_theme(style="white", palette="pastel", font="serif", font_scale=1.1)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='Values', hue='Subcategory', data=data)
plt.title("Value Distribution by Category and Subcategory")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()
