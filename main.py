import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        self.adj_list[node] = []

    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def get_neighbors(self, node):
        return self.adj_list[node]

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.adj_list}
    distances[start] = 0
    pq = [(0, start)]  # 우선순위 큐
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.get_neighbors(current_node):
            distance = current_dist + 1  # 간선 가중치가 1이라고 가정
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

import networkx as nx
import matplotlib.pyplot as plt




