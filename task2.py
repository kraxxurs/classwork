import csv

participants = []
groups = []

for i in range(150):
    row = []
    for j in range(150):
        row.append(0)
    participants.append(row)

with open("graphy/task2.csv", newline = "") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p1 = int(row["from"])
        p2 = int(row["to"])
        participants[p1][p2] = 1

for i in range(len(participants)):
    new_group = [i]
    for j in range(len(participants[i])):
        if participants[i][j] == 1:
            for k in new_group:
                if participants[j][k] == 0:
                    break
            else:  
                new_group.append(j)
    groups.append(new_group)

print(f"Количество групп: {len(groups)}")

for i in range(len(groups)):
    with open(f"graphy/task2_files/{i}_task2.txt", "w") as file:
        for j in range(len(groups[i])):
            file.write(str(groups[i][j]))
            file.write("\n")

    file.close()
