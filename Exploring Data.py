import numpy as np
import pandas as pd

# Student grades data
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]

# Create a NumPy array
grades = np.array(data)
print(grades)

# Additional data on study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D NumPy array
student_data = np.array([study_hours, grades])

# Convert to Pandas DataFrame
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

# Display DataFrame
df_students 

# Handling missing values
df_students.isnull().sum()
df_students = df_students.dropna(axis=0, how='any')

# Explore data in the DataFrame
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

df_students[df_students.StudyHours > mean_study]
df_students[df_students.StudyHours > mean_study].Grade.mean()

passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students.groupby(df_students.Pass).Name.count())
print(df_students.groupby(df_students.Pass)[['StudyHours', 'Grade']].mean())

df_students = df_students.sort_values('Grade', ascending=False)
df_students
