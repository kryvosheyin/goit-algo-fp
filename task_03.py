import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight=0):
        # adding vertices if they don't exist
        for vertex in [from_vertex, to_vertex]:
            if vertex not in self.vertices:
                self.vertices[vertex] = []

        # adding edges to the graph
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # skipping if current distance is not optimal
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances


def main():

    poltava_transport = Graph()

    edges = [
        ("Автовокзал", "Калініна", 1),
        ("Автовокзал", "Метро", 1),
        ("Автовокзал", "Сади-1", 1.5),
        ("Калініна", "Поліклініка", 1),
        ("Поліклініка", "23 Вересня", 1.5),
        ("23 Вересня", "Мотель", 2),
        ("Мотель", "Фурманова", 2.5),
        ("Фурманова", "Карла Лібкнехта", 3),
        ("Карла Лібкнехта", "Чапаєва", 1),
        ("Чапаєва", "Центральний ринок", 1),
        ("Центральний ринок", "Шевченка", 1.5),
        ("Шевченка", "Центр", 1.5),
        ("Мотель", "Ціолковського", 1),
        ("Ціолковського", "Сади-2", 2),
        ("Сади-2", "Огнівка", 2),
        ("Мотель", "Боженка", 3),
        ("Боженка", "Склозавод", 1.5),
        ("Склозавод", "Розсошенці", 3),
        ("Сади-2", "Сади-1", 2),
        ("Сади-1", "Великотирнівська", 2.5),
        ("Великотирнівська", "Браїлки", 2),
        ("Браїлки", "Промбаза", 2.5),
        ("Браїлки", "Авіаційне містечко", 3),
        ("Промбаза", "Жовтнева", 3),
        ("Жовтнева", "Центр", 3),
        ("Центр", "1 міська лікарня", 2.5),
        ("1 міська лікарня", "Юрівка", 2),
        ("Юрівка", "Огнівка", 2.5),
        ("Центр", "Бібліотека", 1.5),
        ("Бібліотека", "Мелькомбінат", 2.5),
        ("Мелькомбінат", "Левада", 3),
        ("Мелькомбінат", "Південний вокзал", 1.5),
    ]

    for from_vertex, to_vertex, weight in edges:
        poltava_transport.add_edge(from_vertex, to_vertex, weight)

    start_vertex = "Центр"
    shortest_distances = poltava_transport.dijkstra(start_vertex)

    print(f"Shortest distances from {start_vertex}: \n{shortest_distances}")


if __name__ == "__main__":
    main()
