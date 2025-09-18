import heapq
from collections import deque
from random import*
 
field = []
n = int(input())
m = int(input())
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(n):
    row = []
    for col in range(m):
        row.append(randint(-1, 2))
    field.append(row)

for i in range(len(field)):
    print(field[i])


class Graph(field):
    def __init__(self) -> None:
        self.edges: dict[tuple][list]  = {} 

    def field_to_graph(self, field):
        for x in range(len(field)):
            for y in range(len(field[row])):
                if field[row][col] != -1: 
                    for dir in directions():
                        x_new = x + dir[0]
                        y_new = y + dir[1]
                        
                        if 0 <= x_new <= len(field[row]) and 0 <= y_new <= len(field):
                            self.edges[(x, y)] = [(x_new, y_new)]

                else: continue
