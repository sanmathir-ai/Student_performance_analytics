import numpy as np

# Function to calculate total marks
def calculate_total(marks):
    return np.sum(marks)


# Function to calculate average marks
def calculate_average(marks):
    return np.mean(marks)


# Function to assign grades
def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to check pass or fail
def check_result(marks):
    if all(mark >= 40 for mark in marks):
        return "Pass"
    else:
        return "Fail"