# Student Exam Scores Analysis Project

## Project Overview
This project analyzes student exam scores by examining various factors such as study hours, attendance percentage, and previous performance.  
The primary goal is to filter students based on their results (Pass/Fail), explore the correlation between study habits and academic success, and generate clean, exported datasets for further use.

## Implementation
The project follows a structured data analysis workflow:

- Data Loading: The dataset is imported from student_exam_scores.csv using the Pandas library.  
- Data Analysis:  
  - Initial exploration of data (first rows, column names, and summary statistics).  
  - Filtering students based on a passing threshold (Score > 60).  
  - Calculating average scores grouped by Hours_Studied and Attendance_Per.  
- Data Export: Generating a new file high_exam_scores.csv containing only the records of students who passed.

## Tools & Technologies
- Python: Core programming language used for logic and analysis.  
- Pandas: Primary library for data manipulation and statistical calculations.  
- VS Code: The integrated development environment (IDE) used for writing and debugging the script.

## Project Files
- exam_scores.py: The main Python script containing the analysis logic.  
- student_exam_scores.csv: The raw input dataset used for the study.  
- requirements.txt: A file listing the necessary dependencies (e.g., pandas) to run the project.
- 
