import pandas as pd
import functions as fn

DATA_FILE = "students.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 150)


def heading(text):
    print("\n" + "=" * 50)
    print(text)
    print("=" * 50)



students = fn.load_data(DATA_FILE)

heading("STUDENT PERFORMANCE ANALYTICS")

print("Total Students:", len(students))

print("\nStudent Data:")
print(students.head())

students = fn.process_students(students)

heading("RESULTS")

columns = [
    "Rank",
    "Student_ID",
    "Name",
    "Department",
    "Total",
    "Average",
    "Grade",
    "Result"
]

print(students[columns].sort_values("Rank"))

stats = fn.class_statistics(students)

heading("OVERALL PERFORMANCE")

print("Class Average:", stats["class_average"])
print("Highest Average:", stats["highest_name"])
print("Lowest Average:", stats["lowest_name"])
print("Students Passed:", stats["passed"])
print("Students Failed:", stats["failed"])
print("Pass Percentage:", stats["pass_percentage"])

heading("SUBJECT ANALYSIS")

subject_data = fn.subject_analysis(students)

print(subject_data)


heading("TOP 5 STUDENTS")

top = fn.top_performers(students)

print(top)

heading("PROJECT COMPLETED")