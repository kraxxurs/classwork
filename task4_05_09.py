import json
from collections import defaultdict

pointA = int(input("Введите пункт отправления (0-19): "))
pointB = int(input("Введите пункт назначения (0-19): "))
routes = []

with open ("graphy/paths.json", "r", encoding = "utf-8") as file:
    paths: dict[int, list] = json.load(file)

def show(points):
    visited = []
    rout = []
    for point in points:
        if point not in visited:
            if point == pointB:
                with open ("graphy/routes.txt", "a") as file2:
                    file2.write(rout, '\n')
                rout.pop(len(rout))
                break
            visited.append(point)
            rout.append(point)
            show(paths[point])


show(paths[pointA])
