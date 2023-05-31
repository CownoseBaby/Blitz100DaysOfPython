# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
student_height_count = 0
student_height_sum = 0
for student in student_heights:
    student_height_count += 1
    student_height_sum += student
    # print(student)
    # print(student_height_count)

student_average_height = round(student_height_sum / student_height_count)
print(student_average_height)