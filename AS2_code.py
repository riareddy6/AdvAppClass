# Course: IT3883, Section 01
# Student Name: Ria Reddy
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose: Reads the student names and scores given in the test input file. Calculates
# each student's final average. Displays results in descending order by grade.





student_averages = []

# OPEN / READ
input_file = open("Assignment2input.txt", "r")

# For each student
for line in input_file:
    student_data = line.split()
    student_name = student_data[0]
    scores = []

    #Data convert
    for score in student_data[1:]:
        scores.append(float(score))
    final_average = sum(scores) / len(scores)
    student_averages.append([student_name, final_average])
input_file.close()


def get_average(student):
    return student[1]

# sorting logic
student_averages.sort(key=get_average, reverse=True)

# DISPLAY
for student in student_averages:
    print(student[0], format(student[1], ".2f"))
