from queue import Queue
class Graph():
    def __init__(self,Nodes):                                   #This method initialises the adjacency list empty
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:                                 #This loop adds vertices as keys in adjacency list and creates no connections
            self.adj_list[node]=[]

    def add_edge(self,u,v):
        self.adj_list[u].append(v)                              #It adds U-V edge in graph
        self.adj_list[v].append(u)

    def print_adj_list(self):
        for node in self.adj_list:
            print(node," --> ",self.adj_list[node])
nodes=[]
n=int(input())
for i in range(1,n+1):
    nodes.append(i)
graph=Graph(nodes)

all_edges=[]                            #All connections between the vertices
for i in range(n-1):
    x,y=list(map(int,input().split()))
    all_edges.append((x,y))
for u,v in all_edges:
    graph.add_edge(u,v)


#Finding levels of program
level={}
queue=Queue()
visited={}
parent={}
for node in graph.adj_list.keys():
    level[node]=-1
    visited[node]=False
    parent[node]=None

source= 1
visited[source]=True
level[source]=0
queue.put(source)

while not queue.empty():
    x=queue.get()
    for vertice in graph.adj_list[x]:
        if not visited[vertice]:
            visited[vertice]=True
            level[vertice]=level[x]+1
            parent[vertice]=x
            queue.put(vertice)

a=[]
b=[]
for value in level.values():
    if value % 2 == 0:
        a.append(value)
    else:
        b.append(value)

ans=(len(a)*len(b))-(n-1)
print(ans)
