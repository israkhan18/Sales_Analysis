import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:\\your_path_here/sales.csv'

data = pd.read_csv(file_path)

print(data.head())

file_path = r'C:\your_path_here/sales_data.csv'  # Update the path
data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data['sales'], bins=20, kde=True)
plt.title('Sales Distribution')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

sales_per_product = data.groupby('product')['sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='sales', y='product', data=sales_per_product)
plt.title('Total Sales per Product')
plt.xlabel('Total Sales')
plt.ylabel('Product')
plt.show()

