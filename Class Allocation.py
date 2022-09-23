"""

You are assigned to allocate classrooms to courses. You are given n courses numbered from 1, 2, ...., n along with the array A, where Ai is the number of students registered in the course i. You are also given m classrooms numbered from 1, 2, ...., m along with the array B, where Bi is the seating capacity of the room i. Each classroom can be assigned to at max one course. Also, classroom i can be assigned to course j only if there is enough seating capacity in classroom i for all the students taking course j, i.e. Bi ≥ Aj.

Find the maximum number of courses that can be scheduled according to the above constraints.

Input Format:
The first line contains two space separated integers n and m (1 ≤ n ≤ 500).
The second line contains n space separated integers A1, A2, ...., An (1 ≤ Ai ≤ 109).
The third line contains m space separated integers B1, B2, ...., Bm (1 ≤ Bi ≤ 109).

Output Format:
Output a single integer, the maximum number of courses that can be scheduled.

"""

def bfs(n,adj_matrix,s,t,parent):
    queue=[s]
    visited=[0 for i in range(n)]
    visited[s]=1
    while len(queue)>0:
        u = queue.pop(0)
        for i in range(n):
            if not visited[i] and adj_matrix[u][i] > 0:
                queue.append(i)
                visited[i] =1
                parent[i] = u
                if i == t:
                    return True
    return False

def ford_fulkerson(n,adj_matrix,s,t):
    parent=[-1 for i in range(n)]
    max_flow=0
    while bfs(n,adj_matrix,s,t,parent):
        flow=float("Inf")
        node=t
        while node != s:
            flow=min(flow,adj_matrix[parent[node]][node])
            node=parent[node]
        max_flow+=flow
        v=t
        while v !=s:
            u = parent[v]
            adj_matrix[u][v] -= flow
            adj_matrix[v][u] += flow
            v= parent[v]
    return max_flow


if __name__ == "__main__":
    n,m=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    adj_matrix=[[0 for i in range(n+m+2)] for j in range(n+m+2)]

    #Source Vertex
    for i in range(1,n+1):
        adj_matrix[0][i]=1

    #Sink Vertex
    for i in range(n+1,n+m+1):
        adj_matrix[i][n+m+1]=1

    #Middle Edges
    for i in range(1,n+1):
        for j in range(n+1,n+m+1):
            if A[i-1] <= B[j-n-1]:
                adj_matrix[i][j]=1
    print(ford_fulkerson(n+m+2,adj_matrix,0,n+m+1))

