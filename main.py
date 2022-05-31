from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def insertEdge(self, u, v):
        self.graph[u].append(v)

    def checkRoute(self, s, d):
        visited = [False] * self.vertices

        queue = list()
        queue.append(s)

        visited[s] = True

        while queue:

            n = queue.pop(0)

            if n == d:
                return True

            for i in self.graph[n]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False


example_graph = Graph(4)
example_graph.insertEdge(0, 1)
example_graph.insertEdge(0, 2)
example_graph.insertEdge(1, 3)
example_graph.insertEdge(2, 3)
example_graph.insertEdge(3, 3)

s = 0
d = 3

if example_graph.checkRoute(s, d):
    print(f'There is a route between {s} and {d}')
else:
    print(f'There is no a route between {s} and {d}')
