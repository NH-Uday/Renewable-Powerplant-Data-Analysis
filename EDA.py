import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
df = pd.read_csv('data/processed_data.csv')

# Basic statistics
print(df.describe())

# Distribution of energy sources
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Energy Source', order=df['Energy Source'].value_counts().index)
plt.title('Distribution of Renewable Energy Sources')
plt.xticks(rotation=45)
plt.show()

# Capacity over time (by energy type)
df['Year'] = pd.to_datetime(df['Commissioning Date']).dt.year
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Capacity (MW)', hue='Energy Source')
plt.title('Installed Capacity over Time by Energy Type')
plt.show()
