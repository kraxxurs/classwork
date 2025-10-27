import math
#R = int(input("Center radius: "))
R = 5
vertices = []
edges = []


class Type():
    def __init__(self, name, transmission, cost):
        self.name = name
        self.transmission = transmission * 2**20
        self.cost = cost


type_A = Type("A", 250, 10000) # 10000 rub za 1000 m
type_B = Type("B", 170, 9000)
type_C = Type("C", 150, 7500)


class Sensor(): 
    def __init__(self, name: str, coords: list, type: str):
        self.name = name
        self.coords = [coords[0] * 5, coords[1] * 5]
        self.type = type

        if self.type == type_A.name:
            self.transmission = type_A.transmission
            self.cost = type_A.cost
        if self.type == type_B.name:
            self.transmission = type_B.transmission
            self.cost = type_B.cost
        if self.type == type_C.name:
            self.transmission = type_C.transmission
            self.cost = type_C.cost

        vertices.append(self)

    def find_connected_components(self):
        pass


class Center(): 
    def __init__(self, R, name, coords):
        self.R = R
        self.name = name
        self.coords = [coords[0] * 5, coords[1] * 5]
        

class Edge():
    def __init__(self, start: Sensor, end: Sensor):
        self.start = start
        self.end = end
        self.weight = math.sqrt((end.coords[0] - start.coords[0])**2 + (end.coords[1] - start.coords[1])**2)
        edges.append(self)

    def __lt__ (self, other):
        return self.weight < other.weight
    
    def calculate_final_cost(self):
        if self.start.transmission > self.end.transmission:
            self.cost = self.start.cost
            self.transmission = self.start.transmission
        else: 
            self.cost = self.end.cost
            self.transmission = self.end.transmission

        final_cost = self.cost * self.weight


class UnionFind():
    def __init__(self, vertices):
        self.root = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        if self.root[vertex] != vertex:
            self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    
    def union(self, start: Center, end: Center):
        root_start = self.find(start)
        root_end = self.find(end)

        if root_start != root_end:
            self.root[root_start] = root_end
            return True
        
        return False


def kraskal (vertices, edges):
    mst = []
    uf = UnionFind(vertices)

    edges.sort()
    for edge in edges:
        uf.union(edge.start, edge.end)

s1 = Sensor("Abc", [1, 1], "A")
s2 = Sensor("Bcd", [2, 2], "B")
s3 = Sensor("Cde", [3, 5], "C")
s4 = Sensor("Def", [7, 2], "A")
s5 = Sensor("Efg", [3, 8], "B")
s6 = Sensor("Fgh", [4, 1], "C")
s7 = Sensor("Ghi", [5, 9], "A")
s8 = Sensor("Hij", [8, 2], "B")
s9 = Sensor("Ijk", [2, 7], "C")
s10 = Sensor("Jkl", [6, 6], "A")

e_1_2 = Edge(s1, s2)
e_2_3 = Edge(s2, s3)
e_3_4 = Edge(s3, s4)
e_4_5 = Edge(s4, s5)
e_7_8 = Edge(s7, s8)
e_8_9 = Edge(s8, s9)
e_9_10 = Edge(s9, s10)

e_1_7 = Edge(s1, s7)
e_3_7 = Edge(s3, s7)
e_6_8 = Edge(s6, s8)
e_2_9 = Edge(s2, s9)
e_2_6 = Edge(s2, s6)
e_2_5 = Edge(s2, s5)

kraskal(vertices, edges)
