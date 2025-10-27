# Kraskal

class Edge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__ (self, other):
        return self.weight < other.weight
    

class UnionFind():
    def __init__(self, vertices):
        self.root = {vertex: vertex for vertex in vertices}

    def find(self, vertex): # поиск корня
        if self.root[vertex] != vertex:
            self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    
    def union(self, start, end):
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
        if uf.union(edge.start, edge.end):
            mst.append(edge) 

    return mst


vertices = ["A", "B", "C"]
edges = [
    Edge("A", "B", 5),
    Edge("B", "C", 7)
]

kraskal(vertices, edges)