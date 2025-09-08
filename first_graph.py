import heapq
from collections import deque

class City():
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __str__(self):
        return f"City {self.index} {self.name}"
    

class Graph():
    def __init__(self) -> None:
        self.cities = {} # индекс -> объект Город
        self.edges = {} # объект Город -> список [[Город, вес]]

    def add_city(self, index, name):
        if index not in self.cities:
            city = City(index, name)
            self.cities[index] = city
            self.edges[city] = []

        else:
            print("error")

    def add_edge(self, index_v, index_u, weight):
        city_v = self.cities.get(index_v)
        city_u = self.cities.get(index_u)

        if not city_v or not city_u:
            print("error")
            return
        
        if city_u is city_v: 
            self.edges[city_u].append((city_u, weight))
            return
        
        else: 
            self.edges[city_v].append((city_u, weight))
            self.edges[city_u].append((city_v, weight))

    def __str__(self):
        result = ""
        for city, neighbours in self.edges.items():
            n_info = ", ".join([f"{c.name} {w}" for c, w in neighbours])
            result += f"{city.name} | {n_info}\n"
        return result


g = Graph()
g.add_city("1", "Moscow")
g.add_city("2", "Kirov")
g.add_city("3", 'Omsk')

g.add_edge("1", "2", 8)
g.add_edge("2", "3", 5)

print(g)
