import pandas as pd
from pathlib import Path

# Read the dataset
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "data" / "Amazon.csv")

# 1. Dataset shape
print("\n1. DATASET SHAPE")
print("Rows and columns:", df.shape)
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# 2. Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# 3. Dataset information
print("\n3. DATASET INFORMATION")
df.info()

# 4. Statistical description
print("\n4. DATASET DESCRIPTION")
print(df.describe()

# 5. Missing values
print("\n5. MISSING VALUES")
print(df.isnull().sum())

# 6. Total missing values
print("\nTotal missing values:", df.isnull().sum().sum())

# 7. Duplicate rows
print("\n6. DUPLICATE ROWS")
print("Total duplicate rows:", df.duplicated().sum())

# 8. Duplicate Order IDs
print("\n7. DUPLICATE ORDER IDs")
print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())

# 9. Data types
print("\n8. DATA TYPES")
print(df.dtypes)

# 10. First five records
print("\n9. FIRST FIVE RECORDS")
print(df.head())
