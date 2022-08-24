class Graph():
    def __init__(self,Nodes):                                   #This method initialises the adjacency list empty
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:                                 #This loop adds vertices as keys in adjacency list and creates no connections
            self.adj_list[node]=[]

    def add_edge(self,u,v):
        self.adj_list[u].append(v)                              #It adds U-V edge in graph
        self.adj_list[v].append(u)                              #It adds V-U edge in graph

    def degree(self,node):
        deg=len(self.adj_list[node])                            #Counting the number of elements in list of a given node
        print("degree of ",node," : ",deg)

    def print_adj_list(self):
        for node in self.adj_list:
            print(node," --> ",self.adj_list[node])

nodes=[1,2,3,4,5,6,7]
graph=Graph(nodes)

all_edges=[(1,4),(1,5),(2,3),(2,6),(2,7)]                       #All connections between the vertices
for u,v in all_edges:
    graph.add_edge(u,v)


vertice=int(input())
graph.print_adj_list()
graph.degree(vertice)
