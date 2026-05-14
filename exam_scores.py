import pandas as pd

df = pd.read_csv('student_exam_scores.csv')

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df['exam_score'].describe())

print(df['exam_score'].unique())

print(df.isnull().sum())

students_passed = df[df['exam_score'] > 60]

print(students_passed)

students_failed = df[df['exam_score'] < 60]

print(students_failed)

A = df.groupby(['hours_studied', 'attendance_percent'])['exam_score'].mean()
print(A)