"""
We have discovered the fastest communication medium Bytelandian scientists announced, and they called it blingors. The blingors are incomparably better than other media known before. Many companies in Byteland started to build blingors networks, so the information society in the kingdom of Bytes is fact! The priority is to build the core of the blingors network, joinig main cities in the country. Assume there is some number of cities that will be connected at the beginning. The cost of building blingors connection between two cities depends on many elements, but it has been successfully estimated. Your task is to design the blingors network connections between some cities in this way that between any pair of cities is a communication route. The cost of this network should be as small as possible.

Remarks:
Input
s [number of test cases <= 10]
n [number of cities <= 10 000]
NAME [city name]
p [number of neigbouring cities to the city NAME]
neigh cost 
     [neigh - the unique number of  city from the main list
      cost - the cost of building the blingors connection from NAME to neigh]
[empty line between test cases]


Output
[separate lines] cost [the minimum cost of building the blingors network]

Example
Input:
2

4
gdansk
2
2 1
3 3
bydgoszcz
3
1 1
3 1
4 4
torun
3
1 3
2 1
4 1
warszawa
2
2 4
3 1

3
ixowo
2
2 1
3 3
iyekowo
2
1 1
3 7
zetowo
2
1 3 
2 7


Output:
3
4
"""

import sys
from heapq import heappush,heappop

def prims(graph,start,parent,distance,visited):
    bag=[]
    min_cost=0
    heappush(bag,(0,start))
    distance[start]=0
    parent[start]=-1
    while bag:
        d,n = heappop(bag)
        if not visited[n]:
            visited[n]=1
            for cd,cn in graph[n]:
                if distance[cn] > cd:
                    parent[cn]=n
                    distance[cn]=cd
                    heappush(bag,(cd,cn))
    for vertices in distance:
        min_cost+=distance[vertices]

    print(min_cost)


t=int(input())
while t!=0:
    print()
    edge_list=[]
    n=int(input())
    for i in range(1,n+1):
        name=str(input())
        p=int(input())
        for j in range(p):
            v,d = list(map(int,input().split()))
            edge_list.append([i,v,d])
    graph={}
    distance={}
    visited={}
    parent={}
    inf=sys.maxsize
    for i in range(1,n+1):
        graph[i]=[]
        distance[i]=inf
        visited[i]=0
        parent[i]=None

    for u,v,d in edge_list:
        graph[u].append([d,v])
        graph[v].append([d,u])

    start=1
    prims(graph,start,parent,distance,visited)
    t-=1
