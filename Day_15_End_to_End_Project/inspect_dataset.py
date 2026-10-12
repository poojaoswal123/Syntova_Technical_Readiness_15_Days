
import pandas as pd

# Read the CSV dataset
file_path = "data/Amazon.csv"
df = pd.read_csv(file_path)

# Display basic dataset information
print("Dataset loaded successfully!")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display first five records
print("\nFirst five records:")
print(df.head())

# Display data types and non-null counts
print("\nDataset information:")
df.info()

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Display numerical statistics
print("\nNumerical summary:")
print(df.describe())
