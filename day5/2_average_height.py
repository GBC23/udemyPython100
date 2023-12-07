# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
# print(student_heights)
print('total height = ', sum(student_heights))
print('number of students = ', len(student_heights) )
print('average height = ', round(sum(student_heights)/len(student_heights)))