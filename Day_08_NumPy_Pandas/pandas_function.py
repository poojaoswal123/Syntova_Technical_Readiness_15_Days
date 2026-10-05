# PANDAS: BASIC TO INTERMEDIATE

import pandas as pd
import numpy as np

# 1. Create a Pandas Series
marks = pd.Series([80, 75, 90, 85, 95])

print("Series:")
print(marks)

# 2. Access Series values
print("First value:", marks[0])
print("First three values:")
print(marks[:3])

# 3. Create a DataFrame
data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Amit", "Priya", "Rahul", "Sneha", "Neha", "Kiran", "Rohit", "Pooja"],
    "department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "salary": [75000, 60000, 85000, 70000, 90000, 62000, 80000, 88000],
    "city": ["Pune", "Mumbai", "Pune", "Kolhapur", "Mumbai", "Pune", "Mumbai", "Kolhapur"],
    "experience": [2, 1, 3, 2, 4, 1, 5, 3]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# 4. View first and last rows
print("First 5 rows:")
print(df.head())

print("First 3 rows:")
print(df.head(3))

print("Last 5 rows:")
print(df.tail())

# 5. Check DataFrame shape
print("Shape:", df.shape)

# 6. Check columns
print("Columns:", df.columns)

# 7. Check data types
print("Data types:")
print(df.dtypes)

# 8. Get DataFrame information
df.info()

# 9. Statistical summary
print("Statistical summary:")
print(df.describe())

# 10. Select one column
print("Employee names:")
print(df["name"])

# 11. Select multiple columns
print("Name and salary:")
print(df[["name", "salary"]])

# 12. Select rows using loc
print("Using loc:")
print(df.loc[0:3, ["name", "salary"]])

# 13. Select rows using iloc
print("Using iloc:")
print(df.iloc[0:3, 1:4])

# 14. Filter rows
high_salary = df[df["salary"] > 75000]

print("Employees with salary above 75000:")
print(high_salary)

# 15. Filter using multiple conditions
it_employees = df[
    (df["department"] == "IT") &
    (df["salary"] > 80000)
]

print("IT employees with salary above 80000:")
print(it_employees)

# 16. Filter using OR condition
pune_or_mumbai = df[
    (df["city"] == "Pune") |
    (df["city"] == "Mumbai")
]

print("Employees from Pune or Mumbai:")
print(pune_or_mumbai)

# 17. Filter using isin()
selected_departments = df[
    df["department"].isin(["IT", "HR"])
]

print("IT and HR employees:")
print(selected_departments)

# 18. Filter using string methods
print("Names starting with P:")
print(df[df["name"].str.startswith("P")])

# 19. Sort by salary
salary_sorted = df.sort_values("salary", ascending=False)

print("Employees sorted by salary:")
print(salary_sorted)

# 20. Sort by multiple columns
sorted_data = df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)

print("Sorted by department and salary:")
print(sorted_data)

# 21. Create a new column
df["bonus"] = df["salary"] * 0.10

print("DataFrame with bonus:")
print(df)

# 22. Create a column using conditions
df["salary_level"] = np.where(
    df["salary"] >= 80000,
    "High",
    "Normal"
)

print("Salary level:")
print(df[["name", "salary", "salary_level"]])

# 23. Rename columns
renamed_df = df.rename(
    columns={"name": "employee_name"}
)

print("Renamed column:")
print(renamed_df.head())

# 24. Drop a column
temp_df = df.drop(columns=["salary_level"])

print("After dropping column:")
print(temp_df.head())

# 25. GroupBy - average salary
average_salary = df.groupby("department")["salary"].mean()

print("Average salary by department:")
print(average_salary)

# 26. GroupBy - total salary
total_salary = df.groupby("department")["salary"].sum()

print("Total salary by department:")
print(total_salary)

# 27. GroupBy - employee count
employee_count = df.groupby("department")["employee_id"].count()

print("Employee count by department:")
print(employee_count)

# 28. GroupBy with multiple calculations
summary = df.groupby("department")["salary"].agg(
    ["count", "mean", "min", "max", "sum"]
)

print("Department salary summary:")
print(summary)

# 29. Check missing values
print("Missing values:")
print(df.isnull().sum())

# 30. Create sample missing data
missing_df = pd.DataFrame({
    "name": ["Amit", "Priya", "Rahul", "Sneha"],
    "salary": [75000, np.nan, 85000, np.nan],
    "city": ["Pune", "Mumbai", None, "Kolhapur"]
})

print("Data with missing values:")
print(missing_df)

# 31. Fill missing values
missing_df["salary"] = missing_df["salary"].fillna(
    missing_df["salary"].mean()
)

missing_df["city"] = missing_df["city"].fillna("Unknown")

print("After filling missing values:")
print(missing_df)

# 32. Remove rows containing missing values
clean_df = missing_df.dropna()

print("After removing missing rows:")
print(clean_df)

# 33. Check duplicate rows
print("Number of duplicate rows:", df.duplicated().sum())

# 34. Remove duplicate rows
df = df.drop_duplicates()

# 35. Find unique values
print("Departments:")
print(df["department"].unique())

# 36. Count unique values
print("Number of departments:")
print(df["department"].nunique())

# 37. Count frequency of values
print("Employees per city:")
print(df["city"].value_counts())

# 38. Merge two DataFrames
department_locations = pd.DataFrame({
    "department": ["IT", "HR", "Finance", "Marketing"],
    "location": ["Pune", "Mumbai", "Kolhapur", "Delhi"]
})

merged_df = pd.merge(
    df,
    department_locations,
    on="department",
    how="left"
)

print("Merged DataFrame:")
print(merged_df)

# 39. Create a date column
date_df = pd.DataFrame({
    "employee": ["Amit", "Priya", "Rahul", "Sneha"],
    "joining_date": [
        "2026-01-10",
        "2026-03-15",
        "2026-06-20",
        "2026-08-05"
    ]
})

# 40. Convert column to datetime
date_df["joining_date"] = pd.to_datetime(
    date_df["joining_date"]
)

print("Date DataFrame:")
print(date_df)

# 41. Extract year, month and day
date_df["year"] = date_df["joining_date"].dt.year
date_df["month"] = date_df["joining_date"].dt.month
date_df["day"] = date_df["joining_date"].dt.day

print("Date information:")
print(date_df)

# 42. Read a CSV file
# csv_df = pd.read_csv("employees.csv")
# print(csv_df.head())

# 43. Save DataFrame to CSV
df.to_csv("employees_output.csv", index=False)

print("CSV file saved successfully.")

# 44. Reset index
filtered_df = df[df["salary"] > 70000]

filtered_df = filtered_df.reset_index(drop=True)

print("Reset index:")
print(filtered_df)

# 45. Apply a function to a column
df["salary_after_increment"] = df["salary"].apply(
    lambda salary: salary * 1.10
)

print("Salary after 10% increment:")
print(df[["name", "salary", "salary_after_increment"]])

# 46. Conditional selection using query()
query_result = df.query(
    "salary > 75000 and department == 'IT'"
)

print("Query result:")
print(query_result)

# 47. Find maximum and minimum values
print("Highest salary:", df["salary"].max())
print("Lowest salary:", df["salary"].min())

# 48. Find row with highest salary
highest_salary_employee = df.loc[
    df["salary"].idxmax()
]

print("Employee with highest salary:")
print(highest_salary_employee)

# 49. Correlation between numerical columns
print("Correlation:")
print(
    df[["salary", "experience"]].corr()
)

# 50. Final practical analysis
print("Average salary:", df["salary"].mean())
print("Total salary:", df["salary"].sum())
print("Highest salary:", df["salary"].max())
print("Lowest salary:", df["salary"].min())

print("Department-wise average salary:")
print(
    df.groupby("department")["salary"].mean()
)