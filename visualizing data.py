import pandas as pd
from matplotlib import pyplot as plt

# Load data from a text file
df_students = pd.read_csv('https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv', delimiter=',', header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the grade needed to pass
passes = pd.Series(df_students['Grade'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

# Visualizing data with Matplotlib
plt.bar(x=df_students.Name, height=df_students.Grade, color='orange')
plt.title('Student Grades')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(rotation=90)
plt.show()

# Getting started with statistical analysis
var_data = df_students['Grade']
fig = plt.figure(figsize=(10, 4))
plt.hist(var_data)
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Measures of central tendency
min_val = var_data.min()
max_val = var_data.max()
mean_val = var_data.mean()
med_val = var_data.median()
mod_val = var_data.mode()[0]

print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val, mean_val, med_val, mod_val, max_val))

fig = plt.figure(figsize=(10, 4))
plt.hist(var_data)
plt.axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
plt.axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
plt.axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
plt.axvline(x=mod_val, color='yellow', linestyle='dashed', linewidth=2)
plt.axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Box plot
fig = plt.figure(figsize=(10, 4))
plt.boxplot(var_data, vert=False)
plt.title('Data Distribution')
plt.show()

# Combining histogram and box plot
def show_distribution(var_data):
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequency')
    ax[0].axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mod_val, color='yellow', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)

    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')
    fig.suptitle('Data Distribution')
    fig.show()

show_distribution(var_data)

# Density plot
fig = plt.figure(figsize=(10, 4))
var_data.plot.density()
plt.title('Data Density')
plt.axvline(x=var_data.mean(), color='cyan', linestyle='dashed', linewidth=2)
plt.axvline(x=var_data.median(), color='red', linestyle='dashed', linewidth=2)
plt.axvline(x=var_data.mode()[0], color='yellow', linestyle='dashed', linewidth=2)
plt.show()
