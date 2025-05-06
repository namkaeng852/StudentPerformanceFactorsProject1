# Import necessary libraries
import pandas as pd

# Load the dataset
df = pd.read_csv(r'D:\data_project\StudentPerformanceFactors.csv')

# Examine the Dataset
# Checking the first few rows to understand the structure of the data
print(df.head())

# Check data types, non-null counts, and column names to get an overview of the dataset
print(df.info())

# Trim spaces in categorical columns
categorical_columns = ['Teacher_Quality', 'Parental_Involvement',
                       'Access_to_Resources', 'Extracurricular_Activities',
                       'Motivation_Level', 'Internet_Access',
                       'Family_Income', 'School_Type', 'Peer_Influence',
                       'Learning_Disabilities', 'Parental_Education_Level',
                       'Distance_from_Home', 'Gender']
for col in categorical_columns:
    df[col] = df[col].str.strip()  # Trim spaces

# Verify by checking for unique values in categorical columns
print(df[categorical_columns].nunique())

# Check for missing values in the dataset
print('Check null values')
print(df.isnull().sum())

# Replace missing values in categorical columns as specified
df['Teacher_Quality'] = df['Teacher_Quality'].fillna('Medium')
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna('College')
df['Distance_from_Home'] = df['Distance_from_Home'].fillna('Moderate')

# Verify that the missing values have been replaced
print(df[['Teacher_Quality', 'Parental_Education_Level', 'Distance_from_Home']].isnull().sum())
print('Check null values after filling')
print(df.isnull().sum())

# Remove duplicate rows if any
print('Drop duplicates')
df.drop_duplicates(inplace=True)

# Make sure numerical columns are in the correct data type (e.g., float, integer)
print('Ensure Consistent Data Types')
df['Hours_Studied'] = df['Hours_Studied'].astype(float)
df['Sleep_Hours'] = df['Sleep_Hours'].astype(float)
df['Previous_Scores'] = df['Previous_Scores'].astype(float)
df['Exam_Score'] = df['Exam_Score'].astype(float)


# Verify that numerical columns are within reasonable ranges
print('Verify numeric range')
df = df[df['Exam_Score'].between(0, 100)]  # Ensure exam scores are between 0 and 100
df = df[df['Previous_Scores'].between(0, 100)]  # Ensure Previous Scores are between 0 and 100

#Rename the columns for easier understanding
df.rename(columns={
    'Hours_Studied': 'Hours_Studied_per_Week',
    'Attendance': 'Attendance_Percentage',
    'Sleep_Hours': 'Sleep_Hours_per_Night',
    'Tutoring_Sessions': 'Tutoring_Sessions_per_Month',
    'Physical_Activity': 'Physical_Activity_Hours_per_Week'
}, inplace=True)

# Recheck the dataset to ensure everything is correct
print('Recheck the dataset')
print(df.head())  # Check first few rows
print(df.info())  # Check data types and non-null values

# Save the cleaned data to a new file
df.to_csv(r'D:\data_project2\Cleaned_StudentPerformanceFactors.csv', index=False)

print("Data export completed")
