Student Exam Scores Analysis Project
Project
This project analyzes student exam scores using several factors such as study hours, attendance percentage, and previous scores. The goal is to filter students who passed or failed based on their exam scores, analyze the relationship between study habits and scores, and export the clean data.

Implementation
Data Loading: The data is read from student_exam_scores.csv using pandas.

Data Analysis:

Display basic data information (first rows, column names, and summary statistics).

Filter students who scored above 60 (passed) and below 60 (failed).

Calculate the average Exam_score based on Hours_studied and Attendance_per.

Data Export: Export the filtered data of passed students to high_exam_scores.csv.

Tools
Python

pandas (Install with pip install pandas)

VS Code

File
student_exam_scores.csv: Input file containing student data.

exam_scores.py: Python script used for loading, analyzing, and exporting the data.

requirements.txt: File containing the required project dependencies