import os
import pandas as pd
import numpy as np

def load_metadata(metadata_path):
    return pd.read_csv(metadata_path)

def load_csv_files(metadata, folder_path):
    data_frames = []
    
    for _, row in metadata.iterrows():
        file_name = row['filename']
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            data = pd.read_csv(file_path)

            numeric_cols = data.select_dtypes(include=[np.number]).columns
            data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

            battery_impedance = None
            if 'Battery_impedance' in data.columns:
                battery_impedance = np.abs(data['Battery_impedance'].apply(lambda x: complex(x.strip('()')) if isinstance(x, str) else x))
            
            re = row['Re'] if pd.notna(row['Re']) else (np.mean(np.abs(battery_impedance.real)) if battery_impedance is not None else None)
            rct = row['Rct'] if pd.notna(row['Rct']) else (np.mean(np.abs(battery_impedance.imag)) if battery_impedance is not None else None)

            processed_data = {
                "Cycle": row['test_id'],
                "Battery_ID": row['battery_id'],
                "Battery_Impedance": battery_impedance.mean() if battery_impedance is not None else None,
                "Re": re,
                "Rct": rct,
                "Capacity": row['Capacity']
            }
            data_frames.append(processed_data)
    
    return pd.DataFrame(data_frames)

def preprocess_data(dataframe):
    numeric_cols = dataframe.select_dtypes(include=[np.number]).columns
    dataframe[numeric_cols] = dataframe[numeric_cols].fillna(dataframe[numeric_cols].mean())
    return dataframe
