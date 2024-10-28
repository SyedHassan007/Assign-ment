import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Sales': np.random.randint(100, 500, 12),
    'Product_Category': np.random.choice(['A', 'B', 'C'], 12),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 12),
    'Revenue': np.random.randint(1000, 5000, 12)
})
print(data.head())

plt.figure(figsize=(8, 6))
sns.barplot(x='Product_Category', y='Sales', data=data, estimator=np.mean)
plt.title('Average Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Sales')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Sales'], marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sales', y='Revenue', data=data)
plt.title('Sales vs Revenue')
plt.xlabel('Sales')
plt.ylabel('Revenue')
plt.show()

# Count the occurrences of each product category
category_counts = data['Product_Category'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Product Category Distribution')
plt.show()

# Aggregate data by region and product category
stacked_data = data.pivot_table(values='Revenue', index='Product_Category', columns='Region', aggfunc=np.sum)

stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Revenue Composition by Region and Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue')
plt.legend(title='Region')
plt.show()

# Prepare data for cumulative sales by category
cumulative_sales = data.pivot_table(values='Sales', index='Date', columns='Product_Category', aggfunc='sum').cumsum()

cumulative_sales.plot(kind='area', stacked=True, figsize=(10, 6))
plt.title('Cumulative Sales by Product Category Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Sales')
plt.legend(title='Product Category')
plt.show()
