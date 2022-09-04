from heapq import heapify,heappush
import sys
class Graph:
    def __init__(self,Nodes):
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]={}

    def add_edge(self,u,v,w):
        self.adj_list[u][v]=w
        self.adj_list[v][u]=w

    def print_adj_list(self):
        for node in self.adj_list:
            print(f"{node} ----> {self.adj_list[node]}")


def dijkstra(graph,src,dest,nodes,n,t):
    inf=sys.maxsize
    node_data={}
    for node in nodes:
        node_data[node]={'cost':inf}

    node_data[src]['cost']=0
    visited=[]
    temp=src

    try:
        for i in range(n - 1):
            if temp not in visited:
                visited.append(temp)
                min_heap = []
                for j in graph[temp]:
                    if j not in visited:
                        cost = node_data[temp]['cost'] + graph[temp][j]
                        if cost < node_data[j]['cost']:
                            node_data[j]['cost'] = cost
                        heappush(min_heap,(node_data[j]['cost'],j))
            heapify(min_heap)
            temp = min_heap[0][1]

        print(f"#Case {t}:",str(node_data[dest]['cost']))
    except:
        print(f"#Case {t}: unreachable")
if __name__ == '__main__':
    t = int(input())
    for k in range(1,t+1):
        nodes = []
        n,m,s,d = list(map(int,input().split()))
        for i in range(n):
            nodes.append(i)
        connect = []
        for i in range(m):
            u,v,w = list(map(int,input().split()))
            connect.append((u,v,w))
        graph = Graph(nodes)

        for u,v,w in connect:
            graph.add_edge(u,v,w)

        dijkstra(graph.adj_list,s,d,nodes,n,k)



