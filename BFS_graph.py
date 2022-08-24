from queue import Queue
adj_list={
    1:[2,4],
    2:[1,5,7,8,3],
    3:[2,4,9,10],
    4:[1,3],
    5:[2,7,8,6],
    6:[5],
    7:[2,5,8],
    8:[2,5,7],
    9:[3],
    10:[3]
}

visited={}
level={}
parent={}
bfs_traversal_output=[]
queue=Queue()

#Initialisation
for node in adj_list.keys():
    visited[node]= False
    level[node]= -1
    parent[node]= None


source=int(input())
visited[source]=True
level[source]=0
queue.put(source)

while not queue.empty():
    u=queue.get()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            level[v]=level[u]+1
            parent[v]=u
            queue.put(v)

print(bfs_traversal_output)


#Shortest distance from source to vertice
vertice=int(input())
print(f"The shortest distance from {source} to {vertice}: {level[vertice]}")

#shortest path from source to vertice
path=[]
while vertice is not None:
    path.append(vertice)
    vertice = parent[vertice]
path.reverse()
print(f"The path from {source} to {vertice} : {path}")
