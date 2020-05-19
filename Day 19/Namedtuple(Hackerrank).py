from collections import namedtuple
students_no = int(input())
student_scores = 0
for i in range(students_no):
    if i == 0:
        Marks = namedtuple('Marks', input())
    info_list = input().split()
    globals()["student{}".format(i)] = Marks(info_list[0], info_list[1], info_list[2], info_list[3])
for j in range(students_no):
    student_scores += int(globals()["student{}".format(j)].MARKS)
print("%0.2f" % float(student_scores/students_no))