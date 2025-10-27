# Algo Prima
import heapq

def prim (graph, start):
    mst = [] # список ребер
    visited = set() # посещенные вершины
    heap = [] # приоритетная куча

    visited.add(start)

    for neighbour, weight in graph[start]:
        heapq.heappush(heap, (weight, start, neighbour))

    while heap:
        weight, start, end = heapq.heappop(heap)
        if end not in visited:
            visited.add(end)
            mst.append((start, end, weight))

            for neighbour, weight in graph[end]:
                if neighbour not in visited:
                    heapq.heappush(heap, (weight, start, neighbour))

    return mst


graph = {
    "A": [("B", 5), ("F", 9), ("J", 12)],
    "B": [("A", 5), ("C", 7), ("F", 9)],
    "C": [("B", 7), ("F", 4), ("D", 5), ("E", 2)],
    "D": [("C", 5), ("E", 2)],
    "E": [("D", 2), ("C", 2), ("F", 3), ("J", 7)],
    "F": [("A", 7), ("B", 9), ("C", 4), ("E", 3), ("J", 4)],
    "J": [("E", 7), ("F", 4), ("A", 12)]
}

mst = prim(graph, "A")

for start, end, weight in mst:
    print(f"{start} - {end} : {weight}")