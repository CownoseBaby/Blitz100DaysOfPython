student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade
# This is the scoring criteria:
#     Scores 91 - 100: Grade = "Outstanding"
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#     Scores 71 - 80: Grade = "Acceptable"
#     Scores 70 or lower: Grade = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
