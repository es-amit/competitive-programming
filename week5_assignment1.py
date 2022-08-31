# Week 5 Assignment - 1

from queue import Queue
class Directed_Graph:
    def __init__(self,Nodes):
        self.node=Nodes
        self.adj_list={}
        for node in self.node:
            self.adj_list[node]=[]

    def add_directed_edge(self,u,v):
        self.adj_list[u].append(v)

    def print_adj_list(self):
        for node in self.adj_list:
            print(f"{node} -----> {self.adj_list[node]}")



nodes=[]
n=int(input())
for i in range(1,n+1):
    nodes.append(i)

graph=Directed_Graph(nodes)

edges = []
for i in range(1,n+1):
    e = int(input())
    edges.append(e)

for i in range(n):
    if edges[i] == -1:
        root = i+1
        if root in edges:
            child = edges.index(root)+1
            graph.add_directed_edge(root,child)
    else:
        root=i+1
        if root in edges:
            child=edges.index(root)+1
            graph.add_directed_edge(root,child)


visited={}
level={}
parent={}
queue=Queue()

for node in graph.adj_list:
    level[node]=-1
    parent[node]=None
    visited[node]=False

for i in range(n):
    if edges[i] == -1:
        source=i+1
        visited[source]=True
        level[source]=0
        queue.put(source)
        while not queue.empty():
            u = queue.get()
            for v in graph.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    level[v] = level[u] + 1
                    parent[v] = u
                    queue.put(v)


for i in level.keys():
    if level[i] == -1:
        level[i]=level[i-1]

groups={}
for i in level.keys():
    if level[i] not in groups:
        groups[level[i]]=[]
        groups[level[i]].append(i)
    else:
        groups[level[i]].append(i)

print(len(groups.keys()))
