"""
A new prime minister has been elected for the country, ByteLand. Having spend all the time learning maths, he always finds new and weird ways to make decisions. Recently, with the revamping of the road system of the country, he has been asked to provide a plan of breaking some roads from a system of roads. There might be some cities which have multiple roads of different length between them.

He should make a plan such that, the length of the total road broken should be as high as possible. He should also ensure that after breaking the roads, all the cities should still be connected with each other (any city can be visited from another city following a simple path along the route after breaking the roads)



Help him break the roads following the above instruction and tell the maximum length of road that you can break.

Constraints:
Number of cities (n) <= 106
Number of roads (m) <= 106
Weight of edges (wi) <= 106

Input:
- The first line of input contains 2 integers n, m representing the number of cities and the number of bidirectional roads respectively.
- The next m lines contain 3 numbers each, A, B and C. A and B are the 2 cities and C is the length of the bidirectional road between these cities.

Output:
- Print the length of the maximum road length that the new prime minister can break.

Example:
Public TestCases	            Input	              Expected Output	
Test Case 1                   2 13                558\n
                              1 2 78
                              2 1 53
                              2 1 79
                              2 1 92
                              2 1 52
                              1 2 44
                              1 2 8
                              2 1 23
                              2 1 21
                              2 1 37
                              1 2 31
                              1 2 28
                              2 1 20

Test Case 2	                  4 10                 437\n
                              1 2 35
                              2 3 83
                              3 4 60
                              2 3 55
                              4 1 44
                              2 3 17
                              1 4 90
                              1 3 47
                              2 1 30
                              4 2 67
                              
"""
def find(graph,node):
    if graph[node]<0:
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
    if a == b:
        pass
    else:
        answer.append([ta,tb,w])
        if graph[a] < graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b]=graph[b]+graph[a]
            graph[a]=b

    return answer
if __name__=="__main__":
    n,m=list(map(int,input().split()))
    ipt=[]
    total_roads=0
    for i in range(m):
        a,b,c=list(map(int,input().split()))
        total_roads+=c
        ipt.append([a,b,c])

    ipt = sorted(ipt,key=lambda ipt: ipt[2])
    graph=[-1]*(n+1)
    answer=[]
    for u,v,d in ipt:
        ans=union(graph,u,v,d,answer)
    min_cost=0
    for u,v,d in ans:
        min_cost+=d

    print(total_roads-min_cost)

