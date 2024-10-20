from scripts.data_preprocessing import load_data, clean_data, save_processed_data
from scripts.analysis import capacity_by_region

if __name__ == "__main__":
    # File paths
    raw_data_path = 'data/power_plants.csv'
    processed_data_path = 'data/processed_data.csv'

    # Preprocessing data
    print("Loading and cleaning data...")
    data = load_data(raw_data_path)
    clean_data = clean_data(data)
    save_processed_data(clean_data, processed_data_path)

    # Performing analysis
    print("Performing analysis on the cleaned data...")
    capacity_by_region(clean_data)
