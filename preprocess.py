import pandas as pd

# Load raw data
data = pd.read_csv('raw_data.csv')

# Print column names before cleaning
print("Original column names:", data.columns)

# Clean column names by removing parentheses and trailing spaces
data.columns = data.columns.str.replace(r'\(.*\)', '', regex=True).str.strip()

# Print cleaned column names to verify the changes
print("Cleaned column names:", data.columns)

# Normalize numerical fields
if 'Temperature' in data.columns:
    data['Temperature'] = (data['Temperature'] - data['Temperature'].mean()) / data['Temperature'].std()
else:
    print("Column 'Temperature' not found after cleaning")

if 'Wind Speed' in data.columns:
    data['Wind Speed'] = (data['Wind Speed'] - data['Wind Speed'].mean()) / data['Wind Speed'].std()
else:
    print("Column 'Wind Speed' not found after cleaning")

# Save preprocessed data
data.to_csv('processed_data.csv', index=False)
