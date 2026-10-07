import numpy as np
import pandas as pd


subjects = ["Python", "Java", "DBMS", "Web Development", "Data Analytics"]

PASS_MARK = 40
MIN_ATTENDANCE = 75


def load_data(file_path):
    return pd.read_csv(file_path)


def calculate_total(row):
    marks = row[subjects].to_numpy(dtype=float)
    return int(np.sum(marks))


def calculate_average(row):
    marks = row[subjects].to_numpy(dtype=float)
    return round(float(np.mean(marks)), 2)


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def get_result(row):
    for subject in subjects:
        if row[subject] < PASS_MARK:
            return "Fail"
    return "Pass"


def get_attendance_status(attendance):
    if attendance >= MIN_ATTENDANCE:
        return "Regular"
    else:
        return "Low"


def process_students(df):

    totals = []
    averages = []
    grades = []
    results = []
    attendance_status = []

    for index, row in df.iterrows():

        total = calculate_total(row)
        average = calculate_average(row)

        totals.append(total)
        averages.append(average)
        grades.append(get_grade(average))
        results.append(get_result(row))
        attendance_status.append(
            get_attendance_status(row["Attendance"])
        )

    df["Total"] = totals
    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results
    df["Attendance_Status"] = attendance_status

    df["Rank"] = df["Total"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    return df


def class_statistics(df):

    averages = df["Average"].to_numpy()

    highest = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()

    stats = {
        "total_students": len(df),
        "class_average": round(np.mean(averages), 2),
        "median": round(np.median(averages), 2),
        "standard_deviation": round(np.std(averages), 2),
        "highest_name": highest["Name"],
        "highest_average": highest["Average"],
        "lowest_name": lowest["Name"],
        "lowest_average": lowest["Average"],
        "passed": passed,
        "failed": failed,
        "pass_percentage": round((passed / len(df)) * 100, 2),
        "average_attendance": round(df["Attendance"].mean(), 2)
    }

    return stats


def subject_analysis(df):

    result = []

    for subject in subjects:

        marks = df[subject].to_numpy()

        data = {
            "Subject": subject,
            "Average": round(np.mean(marks), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Passed": int(np.sum(marks >= PASS_MARK)),
            "Failed": int(np.sum(marks < PASS_MARK)),
            "Topper": df.loc[df[subject].idxmax(), "Name"]
        }

        result.append(data)

    return pd.DataFrame(result)


def top_performers(df, number=5):

    columns = [
        "Rank",
        "Student_ID",
        "Name",
        "Department",
        "Total",
        "Average",
        "Grade"
    ]

    return df.sort_values(
        by="Total",
        ascending=False
    ).head(number)[columns]