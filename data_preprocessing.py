import pandas as pd

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Cleans the dataset by handling missing values, formatting, etc."""
    # Handle missing values
    df.fillna(value={'Capacity (MW)': df['Capacity (MW)'].median()}, inplace=True)
    
    # Convert date columns to datetime objects
    df['Commissioning Date'] = pd.to_datetime(df['Commissioning Date'], errors='coerce')
    
    # Normalize categorical values
    df['Energy Source'] = df['Energy Source'].str.lower()
    
    return df

def save_processed_data(df, output_path):
    """Save the cleaned dataset."""
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # File paths
    raw_data_path = 'data/power_plants.csv'
    processed_data_path = 'data/processed_data.csv'
    
    # Load and clean data
    data = load_data(raw_data_path)
    clean_data = clean_data(data)
    
    # Save processed data
    save_processed_data(clean_data, processed_data_path)
