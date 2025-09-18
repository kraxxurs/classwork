import heapq
from collections import deque

class City:
    def __init__(self, index, name):
        self.index=index
        self.name=name
    
    def __str__(self):
        return f'City {self.index}{self.name}'
    
class Graph:
    def __init__(self):
        self.cities={} #index -> объект Город
        self.edges={} #объект город -Ю список [(город, вес)]

    def add_city(self, index, name):
        if index not in self.cities:
            city = City(index, name)
            self.cities[index]=city
            self.edges[city]=[]
        else:print('Error')
    
    def add_adge(self, index_v, index_u, weight):
        city_v = self.cities.get(index_v)
        city_u = self.cities.get(index_u)
        if not city_u or not city_v:
            print('Error')
            return
        if city_u is city_v:
            self.edges[city_u].append((city_v, weight))
            return
        self.edges[city_u].append((city_v, weight))
        self.edges[city_v].append((city_u, weight))
    def __str__(self):
        result=''
        for  city, neighbors in self.edges.items():
            n_info = ', '.join([f'{c.name}{w}' for c, w in neighbors])
            result+=f'{city.name} | {n_info}\n'
        return result

    def dijkstra(self, start, end):
        distances={index:float('inf') for  index in self.cities}
        distances[start]=0
        route={index: None for index in self.cities}
        points = [(0, start)]
        city=self.cities[start]

        while points and end != city.index:
            current_dist, current_index = heapq.heappop(points)
            city=self.cities[current_index]

            if current_dist > distances[current_index]:
                continue
            for neighbor, weight in self.edges[city]:
                new_distance = current_dist + weight
                if new_distance < distances[neighbor.index]:
                    distances[neighbor.index] = new_distance
                    route[neighbor.index] = current_index
                    heapq.heappush(points, (new_distance, neighbor.index))
        return distances, route
    
    @staticmethod
    def reconstact_path(route, start, end):
        path=[]
        current = end
        while current!= start:
            path.append(current)
            current=route.get(current, None)
            if current == None:
                return None
        path.append(start)
        path.reverse()
        return path






g=Graph()
g.add_city('1', 'Moscow')
g.add_city('2', 'Kirov')
g.add_city('3', 'Omsk')
g.add_city('4', 'qwe')
g.add_city('5', 'asd')
g.add_city('6', 'zxc')
g.add_city('7', 'qwerty')


g.add_adge('1', '2', 3)
g.add_adge('1', '4', 5)
g.add_adge('1', '6', 2)
g.add_adge('2', '3', 5)
g.add_adge('2', '4', 4)
g.add_adge('3', '5', 1)
g.add_adge('3', '4', 10)
g.add_adge('1', '6', 2)
g.add_adge('2', '3', 15)
g.add_adge('2', '4', 4)
g.add_adge('5', '6', 7)
g.add_adge('3', '5', 1)
g.add_adge('3', '4', 10)
g.add_adge('5', '7', 10)
g.add_adge('6', '7', 6)

print(g)
dist, route=g.dijkstra('1', '3')
path=g.reconstact_path(route, '1', '3')
print(path, dist['3'])