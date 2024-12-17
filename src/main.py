import os
import sys
from data_loader import load_metadata, load_csv_files, preprocess_data
from plot_generator import plot_battery_impedance, plot_re, plot_rct

def main():
    # Define the path to the metadata CSV file
    metadata_path = r"C:/Users/hruth/Music/Projects/nasa_battery_analysis/data/metadata.csv"
    
    # Check if the metadata file exists
    if not os.path.exists(metadata_path):
        print(f"Error: The file at {metadata_path} does not exist.")
        return  # Exit if the file is not found
    else:
        print(f"Metadata file found at {metadata_path}")
        metadata = load_metadata(metadata_path)  # Load metadata CSV
    
    # Define the folder path containing the CSV files
    folder_path = r"C:/Users/hruth/Music/Projects/nasa_battery_analysis/data/cleaned_dataset/"
    
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder at {folder_path} does not exist.")
        return  # Exit if the folder is not found
    else:
        print(f"Folder exists: {folder_path}")
    
    # Load CSV files using metadata (if the previous checks passed)
    print("Loading CSV files...")
    data = load_csv_files(metadata, folder_path)  # Load data from CSV files
    print(f"Loaded {len(data)} data files.")

    # Preprocess the loaded data (cleaning and handling missing values)
    print("Preprocessing data...")
    clean_data = preprocess_data(data)
    print(f"Preprocessed data with {len(clean_data)} entries.")

    # Generate plots for the clean data
    print("Generating plots...")
    fig1 = plot_battery_impedance(clean_data)
    print("Battery Impedance plot generated.")
    
    fig2 = plot_re(clean_data)
    print("Electrolyte Resistance (Re) plot generated.")
    
    fig3 = plot_rct(clean_data)
    print("Charge Transfer Resistance (Rct) plot generated.")
    
    # Set the output directory for saving the plots
    OUTPUT_DIR = os.path.join("output", "figures")
    
    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory created at {OUTPUT_DIR}.")

    # Save the plots as HTML files
    fig1.write_html(os.path.join(OUTPUT_DIR, "Battery_Impedance.html"), full_html=True)
    print("Battery Impedance plot saved to HTML.")
    
    fig2.write_html(os.path.join(OUTPUT_DIR, "Re.html"), full_html=True)
    print("Re plot saved to HTML.")
    
    fig3.write_html(os.path.join(OUTPUT_DIR, "Rct.html"), full_html=True)
    print("Rct plot saved to HTML.")
    
    print(f"Plots successfully saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
