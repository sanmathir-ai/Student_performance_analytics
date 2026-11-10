import pandas as pd
import numpy as np

# Read the student dataset
data = pd.read_csv("students.csv")

# Display the student data
print("STUDENT DATASET")
print(data)

# Display column names
print("\nCOLUMN NAMES:")
print(data.columns)

# Display number of records
print("\nNUMBER OF STUDENTS:")
print(len(data))

# Display basic information
print("\nDATASET INFORMATION:")
print(data.info())

# Import functions from functions.py
from functions import calculate_total
from functions import calculate_average
from functions import assign_grade
from functions import check_result

# Define subject columns
subjects = ["Python", "Mathematics", "English"]

# Process student records using a loop
for index, row in data.iterrows():

    # Get student marks
    marks = row[subjects].values

    # Calculate total and average
    total = calculate_total(marks)
    average = calculate_average(marks)

    # Assign grade
    grade = assign_grade(average)

    # Check pass or fail
    result = check_result(marks)

    # Store calculated results
    data.loc[index, "Total"] = total
    data.loc[index, "Average"] = round(average, 2)
    data.loc[index, "Grade"] = grade
    data.loc[index, "Result"] = result

# Display processed data
print("\nSTUDENT PERFORMANCE RESULTS")
print(data)


print("\nSTUDENT PERFORMANCE ANALYSIS")

# Find the highest-performing student
top_student = data.loc[data["Average"].idxmax()]

print("\nTOP PERFORMING STUDENT:")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])

# Find the lowest-performing student
lowest_student = data.loc[data["Average"].idxmin()]

print("\nLOWEST PERFORMING STUDENT:")
print("Name:", lowest_student["Name"])
print("Average:", lowest_student["Average"])

# Calculate subject-wise average
subject_average = data[subjects].mean()

print("\nSUBJECT-WISE AVERAGE:")
print(subject_average)

# Find the best-performing subject
best_subject = subject_average.idxmax()

print("\nBEST PERFORMING SUBJECT:")
print(best_subject)

passed = (data["Result"] == "Pass").sum()
failed = (data["Result"] == "Fail").sum()

print("\nPASS/FAIL STATISTICS:")
print("Passed Students:", passed)
print("Failed Students:", failed)

# Calculate overall class average
class_average = data["Average"].mean()

print("\nOVERALL CLASS AVERAGE:")
print(round(class_average, 2))

print("\n" + "=" * 50)
print("       STUDENT PERFORMANCE FINAL REPORT")
print("=" * 50)

# Display student-wise performance
print("\nSTUDENT-WISE PERFORMANCE:")
print(data[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

# Display subject-wise performance
print("\nSUBJECT-WISE PERFORMANCE:")
for subject, average in subject_average.items():
    print(subject, ":", round(average, 2))

# Display pass and fail statistics
print("\nPASS/FAIL SUMMARY:")
print("Total Students:", len(data))
print("Passed:", passed)
print("Failed:", failed)

# Display top performer
print("\nTOP PERFORMER:")
print(top_student["Name"], "-", top_student["Average"])

# Display lowest performer
print("\nLOWEST PERFORMER:")
print(lowest_student["Name"], "-", lowest_student["Average"])

# Display overall class average
print("\nOVERALL CLASS AVERAGE:", round(class_average, 2))

print("\n" + "=" * 50)
print("          END OF PERFORMANCE REPORT")
print("=" * 50)