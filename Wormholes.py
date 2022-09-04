import sys
def BellmanFord(source,n,edge_list):
    inf=sys.maxsize
    dist=[]
    pred=[]
    for i in range(n):
        dist.append(inf)
        pred.append(-1)
    dist.pop(0)
    dist.insert(0,0)
    for i in range(n-1):
        for u,v,w in edge_list:
            if dist[v] > dist[u]+w:
                dist[v]=dist[u]+w
                pred[v]=u
    for u,v,w in edge_list:
        if dist[v] > dist[u]+w:
            return 0
    return 1

t=int(input())
while t!=0:
    edge_list=[]
    n,m=list(map(int,input().split()))
    for i in range(m):
        u,v,w=list(map(int,input().split()))
        edge_list.append((u,v,w))

    ans = BellmanFord(0,n,edge_list)
    if ans == 1:
        print("not possible")
    else:
        print("possible")
    t-=1
