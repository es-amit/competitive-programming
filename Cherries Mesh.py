def find(graph,node):
    if graph[node] < 0:
        return node
    else:
        temp=find(graph,graph[node])
        graph[node]=temp
        return temp

def union(graph,a,b,w,answer):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        answer.append([ta,tb,w])
        if graph[a] < graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b]=graph[b]+graph[a]
            graph[a]=b
    connected_components=-1
    for v in graph:
        if v < 0:
            connected_components+=1

    return 2*connected_components-2+len(answer)
t=int(input())
for k in range(t):
    n,m=list(map(int,input().split()))
    ipt=[]
    for i in range(m):
        u,v=list(map(int,input().split()))
        ipt.append([u,v,1])
    graph=[-1]*(n+1)

    answer=[]
    for u,v,d in ipt:
        ans=union(graph,u,v,d,answer)
    print(f"Case #{k+1}: {ans}")
