import csv
students_list = []
for i in range(500):
    row = []
    for j in range(500):
        row.append(0)
    students_list.append(row)

with open("graphy/task1.csv", newline = "") as file:
    reader = csv.DictReader(file)
    for row in reader:
        s1 = int(row["student_1"])
        s2 = int(row["student_2"])
        students_list[0][0] = 1
        students_list[s2][s1] = 1

for i in range(len(students_list)):
    print(students_list[i])  
    print("\n")