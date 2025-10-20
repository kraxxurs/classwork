R = int(input("Center radius: "))


class Type():
    def __init__(self, name, transmission, cost):
        self.name = name
        self.transmission = transmission * 2**20
        self.cost = cost


type_A = Type("A", 250, 1000)
type_B = Type("B", 170, 900)
type_C = Type("C", 150, 750)


class Sensor(): 
    def __init__(self, name: str, coords: list, type: str):
        self.name = name
        self.coords = (coords[0] * 5, coords[1] * 5)
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


class Center(): 
    def __init__(self, R, name, coords):
        self.R = R
        self.name = name
        self.coords = (coords[0] * 5, coords[1] * 5)
        

class Edge():
    def __init__(self, start: Center, end: Center):
        self.start = start
        self.end = end
        self.weight = ((end.coords[0] - start.coords[0])**2 + (end.coords[1] - start.coords[1])**2)**(0,5)

    def __lt__ (self, other):
        return self.weight < other.weight


class UnionFind():
    def __init__(self, vertices):
        self.root = {vertex: vertex for vertex in vertices}

    def find(self, vertex): # поиск корня
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


c1 = Center(R, "qwe", (1, 1))

s1 = Sensor("abc", [1, 1], "A")
s2 = Sensor("def", [2, 2], "B")
e_1_2 = Edge(s1, s2)
print(e_1_2.weight)