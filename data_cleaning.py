import pandas as pd

# Load dataset by our team
file_path = "dairy_spoilage_data_2025.csv"  
df = pd.read_csv(file_path)

# Convert 'Manufacture Date' and 'Expiry Date' to datetime format by our team
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])
df['Expiry Date'] = pd.to_datetime(df['Expiry Date'])

# Check for duplicate entries by our team
duplicate_count = df.duplicated().sum()
print(f"\nDuplicate Entries: {duplicate_count}")

# Remove duplicates if any by our team
df = df.drop_duplicates()

# Create a new column for Shelf Life (Expiry Date - Manufacture Date) by our team
df['Shelf Life (Days)'] = (df['Expiry Date'] - df['Manufacture Date']).dt.days

# Check for outliers in 'Storage Temperature' and 'Bacterial Count' by our team
print("\nStorage Temperature (°C) - Summary:")
print(df['Storage Temperature (°C)'].describe())

print("\nBacterial Count (CFU/mL) - Summary:")
print(df['Bacterial Count (CFU/mL)'].describe())

# Save cleaned data by our team
df.to_csv("cleaned_dairy_data.csv", index=False)

print("\n✅ Data Cleaning Completed! Cleaned dataset saved as 'cleaned_dairy_data.csv'.")
