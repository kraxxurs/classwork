import csv

studentX = 0
students_list = []
direct_contact = []
indirect_contact = []

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
        students_list[s1][s2] = 1
        students_list[s2][s1] = 1

for i in range(len(students_list)):
    if students_list[studentX][i] == 1:
        direct_contact.append(i)

for i in range(len(direct_contact)):
    for j in range(len(students_list[i])):
        if students_list[direct_contact[i]][j] == 1 and j != studentX:
            indirect_contact.append(j)

file1 = open("graphy/task1_direct.txt", "w")
for i in range(len(direct_contact)):
    file1.write(str(direct_contact[i]))
    file1.write("\n")

file1.close

file2 = open("graphy/task1_indirect.txt", "w")
for i in range(len(indirect_contact)):
    file2.write(str(indirect_contact[i]))
    file2.write("\n")
file2.close