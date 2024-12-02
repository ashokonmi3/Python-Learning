# Case Study: Analyzing Student Exam Scores with NumPy
# Objective:
# 
# 
# 
# 
# Use NumPy to analyze the exam scores of a group of students.
# We will simulate a dataset of student exam scores, perform various statistical analyses, and visualize the results.

# Scenario:
# Imagine you are a data analyst at a school. The school has conducted exams for 100 students across three subjects: 
# Math, Science, and English. You need to analyze the data to:

# Find the average scores of each student.
# Calculate the subject-wise average scores.
# Identify the highest and lowest scores for each subject.
# Detect students who need improvement(students who scored below 40 in any subject).
# Visualize the distribution of scores for each subject.
# Step 1: Create the Data
# We will simulate the data for 100 students, 
# each with scores in Math, Science, and English. We'll use NumPy to generate this data.










import matplotlib.pyplot as plt
import numpy as np

# Simulate data for 100 students and 3 subjects (Math, Science, English)
np.random.seed(42)  # To ensure reproducibility

# Generate random scores between 0 and 100 for each subject
scores = np.random.randint(0, 101, size=(100, 3))

# Assign column names to each subject
subjects = ['Math', 'Science', 'English']

# Print the first few rows of the scores array to see the data
print("Scores (First 5 students):\n", scores[:5])

# Explanation:
# We generate random integers between 0 and 100 for each student and for each subject.
# scores is a 2D array with dimensions 100x3, where each row represents a student and each column represents a subject.
# Step 2: Calculate Student-wise and Subject-wise Averages
# We now need to calculate the average scores for each student across all subjects, as well as the average score for each subject.
# ==========================================
# Calculate the average score for each student (along axis 1)
student_averages = np.mean(scores, axis=1)

# Calculate the average score for each subject (along axis 0)
subject_averages = np.mean(scores, axis=0)

# Print results
print("Student Averages (First 5 students):\n", student_averages[:5])
print("Subject Averages: Math, Science, English", subject_averages)
# Explanation:
# np.mean(scores, axis=1) computes the average score for each student by taking the mean across the 3 subjects (columns).
# np.mean(scores, axis=0) computes the average score for each subject by taking the mean across all 100 students (rows).
# Step 3: Find Highest and Lowest Scores
# Now, let's find the highest and lowest scores for each subject and each student.
# =========================================
# Find the highest and lowest scores for each subject
subject_max = np.max(scores, axis=0)
subject_min = np.min(scores, axis=0)

# Find the highest and lowest scores for each student
student_max = np.max(scores, axis=1)
student_min = np.min(scores, axis=1)

# Print results
print("Highest scores per subject:", subject_max)
print("Lowest scores per subject:", subject_min)
print("Highest scores per student (First 5):", student_max[:5])
print("Lowest scores per student (First 5):", student_min[:5])
# Explanation:
# np.max(scores, axis=0) and np.min(scores, axis=0) find the highest and lowest scores across all students for each subject.
# np.max(scores, axis=1) and np.min(scores, axis=1) find the highest and lowest scores for each student across all subjects.
# Step 4: Detect Students Needing Improvement
# We can identify students who need improvement by checking if they scored below 40 in any subject.
# ==========================================
# Identify students who scored below 40 in any subject
improvement_needed = np.any(scores < 40, axis=1)

# Get the indices of students who need improvement
students_to_improve = np.where(improvement_needed)[0]

# Print the students who need improvement
print(f"Students who need improvement (IDs): {students_to_improve}")
# Explanation:
# np.any(scores < 40, axis=1) checks if any score in a row (student) is less than 40 in any of the subjects.
# np.where(improvement_needed) gives the indices of students who need improvement.
# Step 5: Visualize the Data
# Let's visualize the distribution of scores for each subject using histograms.
# ==================================================

# Plot histograms for each subject
plt.figure(figsize=(10, 6))

# Histogram for Math
plt.subplot(1, 3, 1)
plt.hist(scores[:, 0], bins=10, color='skyblue', edgecolor='black')
plt.title('Math Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')

# Histogram for Science
plt.subplot(1, 3, 2)
plt.hist(scores[:, 1], bins=10, color='lightgreen', edgecolor='black')
plt.title('Science Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')

# Histogram for English
plt.subplot(1, 3, 3)
plt.hist(scores[:, 2], bins=10, color='salmon', edgecolor='black')
plt.title('English Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')

plt.tight_layout()
plt.show()

# Explanation:
# We use plt.hist() to plot histograms of the scores for each subject.
# The number of bins is set to 10, which helps us visualize the distribution of scores across the subjects.
# plt.subplot() is used to create a grid of subplots, so each subject has its own histogram.
# Summary:
# In this case study, we used NumPy to:

# Generate a simulated dataset of student exam scores across three subjects.
# Calculate various statistics like the average score for each student and subject, as well as the highest and lowest scores.
# Identify students needing improvement based on scores below 40.
# Visualize the score distributions for each subject.
# Key NumPy Concepts Covered:
# Array creation (np.random.randint and np.arange)
# Statistical functions (np.mean, np.max, np.min, np.any)
# Indexing and masking with NumPy
# Histogram plotting using matplotlib
# This case study gives students hands-on experience in analyzing real-world data using NumPy, providing them with valuable skills for data analysis tasks.
