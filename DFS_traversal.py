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

color={}
parent={}
trav_time={}
dfs_traversal_output=[]

for node in adj_list.keys():
    color[node]="W"
    parent[node]=None
    trav_time[node]=[-1,-1]

time=0
def dfs_util(u):
    global time
    color[u]="G"
    trav_time[u][0]=time
    time+=1
    dfs_traversal_output.append(u)
    for v in adj_list[u]:
        if(color[v]=="W"):
            parent[v]=u
            dfs_util(v)
    trav_time[u][1]=time
    time+=1
    color[u]="B"

source=int(input())
dfs_util(source)
print(dfs_traversal_output)

print("Time traversal")
for node in trav_time:
    print(f"{node} --> {trav_time[node]}")
