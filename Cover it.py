from queue import Queue
class Graph():
    def __init__(self,Nodes):                                   #This method initialises the adjacency list empty
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:                                 #This loop adds vertices as keys in adjacency list and creates no connections
            self.adj_list[node]=[]

    def add_edge(self,u,v):
        self.adj_list[u].append(v)                              #It adds U-V edge in graph
        self.adj_list[v].append(u)                              #It adds V-U edge in graph

    def print_adj_list(self):
        for node in self.adj_list:
            print(node," --> ",self.adj_list[node])

nodes=[]
n,m=list(map(int,input().split()))
for i in range(1,n+1):
    nodes.append(i)
graph=Graph(nodes)

all_edges=[]
for i in range(m):
    u,v=list(map(int,input().split()))
    all_edges.append((u,v))

for u,v in all_edges:
    graph.add_edge(u,v)

#BFS algorithm

visited={}
even=[]
odd=[]
level={}
parent={}
bfs_traversal_output=[]
queue=Queue()

#Initialisation
for node in graph.adj_list.keys():
    visited[node]= False
    level[node]= -1
    parent[node]= None


source=1
visited[source]=True
level[source]=0
queue.put(source)

while not queue.empty():
    u=queue.get()
    bfs_traversal_output.append(u)
    for v in graph.adj_list[u]:
        if not visited[v]:
            visited[v]=True
            level[v]=level[u]+1
            parent[v]=u
            queue.put(v)
for i in level.keys():
    if level[i]%2 == 0:
        even.append(i)
    else:
        odd.append(i)

if(len(even) <= len(odd)):
    ans = ' '.join([str(i) for i in even])
    print(len(even),ans,sep="\n")
else:
    ans = ' '.join([str(i) for i in even])
    print(len(odd),ans,sep="\n")
