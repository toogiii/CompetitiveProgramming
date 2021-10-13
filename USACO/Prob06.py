from collections import defaultdict
nodes = []
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, v):
        q = []
        visited = []
        distance = 0
        q.append(v)
        visited.append(v)
        while v != "B":
            v = q.pop(0)
            distance = 0
            print(v, end = " ")
            for i in self.graph[v]:
                if self.graph[v] in visited:
                    q.append(i)
                    visited.append(i)
                    print(q)
                    print(visited)
g = Graph()
grid = [] 
f = 0
for i in range(0, 10):
    line = input()
    appender = []
    for j in range(0, len(line)):
        appender.append(line[j])
    grid.append(appender)
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        f += 1
        if grid[i][j] == "L":
            nodes.extend([i, j])
            print(True)
        else:
            grid[i][j] = f
        for k in range(0, 9):
            pmi = 0
            pmj = 0
            if k - 5 > 0:
                pmi = i - 1
            elif k - 2 > 0:
                pmi = i + 1
            else:
                pmi = i
            if k % 3 == 0:
                pmj = j - 1
            elif k % 3 == 1:
                pmj = j
            elif k % 3 == 2:
                pmj = j + 1
            try:
                if pmi == i and pmj == j:
                    raise IndexError()
                if pmi > 9 or pmi < 0 or pmj > 9 or pmi < 0:
                    raise IndexError()
                if grid[pmi][pmj] != "R":
                    g.addEdge(grid[i][j], grid[pmi][pmj])
                print(pmi, pmj, grid[pmi][pmj])
            except:
                print(False)
                continue
for i in range(0, len(grid)):
    print(grid[i])
print(grid[0][1])
g.BFS(grid[nodes[0]][nodes[1]])
