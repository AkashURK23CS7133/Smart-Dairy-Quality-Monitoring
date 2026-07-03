import pandas as pd

def clean_data(file_path):
    """ Load, clean, and return the processed dataset """
    try:
        df = pd.read_csv(file_path)

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        # Handle missing values (fill with mean for numerical columns)
        df.fillna(df.mean(numeric_only=True), inplace=True)

        # Ensure correct data types
        df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
        df['Humidity'] = pd.to_numeric(df['Humidity'], errors='coerce')
        df['Storage_Time'] = pd.to_numeric(df['Storage_Time'], errors='coerce')

        # Save cleaned data
        cleaned_file_path = "dataset/cleaned_data.csv"
        df.to_csv(cleaned_file_path, index=False)
        return cleaned_file_path, df

    except Exception as e:
        print(f"Error in data cleaning: {e}")
        return None, None
