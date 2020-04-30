class Graph():

    def __init__(self):
        self.__graph__ = {}

    def add_vertex(self, v):
        self.__graph__[v] = []

    def add_edge(self, s, t):
        self.__graph__[s].insert(0, t)
        self.__graph__[t].insert(0, s)

    def dfs(self, start):
        search_stack = []
        visited = set()

        search_stack.append(start)

        while len(search_stack) > 0:
            if search_stack[-1] not in visited:
                print(search_stack[-1], end=' ')

                visited.add(search_stack[-1])

                childrens = self.__graph__[search_stack.pop()]

                search_stack.extend(childrens)
            else:
                search_stack.pop()
                

N, M, V = map(int, input().split())

graph = Graph()

inputs = []

for _ in range(M):
    inputs.append(list(map(int, input().split())))

for i in inputs:
    a, b = i
    graph.add_vertex(a)
    graph.add_vertex(b)

for j in inputs:
    a, b = j
    graph.add_edge(a, b)


print(graph.__graph__)

graph.dfs(V)
