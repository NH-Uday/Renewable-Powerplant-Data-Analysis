import pandas as pd
import matplotlib.pyplot as plt

def load_processed_data(filepath):
    """Load the processed data for analysis."""
    return pd.read_csv(filepath)

def capacity_by_region(df):
    """Analyze total capacity by region."""
    region_capacity = df.groupby('Region')['Capacity (MW)'].sum()
    print(region_capacity)
    
    # Visualize the results
    region_capacity.plot(kind='barh', figsize=(8, 5))
    plt.title('Total Capacity by Region')
    plt.xlabel('Capacity (MW)')
    plt.ylabel('Region')
    plt.show()

if __name__ == "__main__":
    processed_data_path = 'data/processed_data.csv'
    
    # Load the processed data
    data = load_processed_data(processed_data_path)
    
    # Analyze capacity by region
    capacity_by_region(data)
