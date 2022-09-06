"""Couple in Workspace

There is a couple who is madly in love, but due to the upcoming semester exams, they need to study in the workspace. The workspace has chairs in form of a N×M matrix.

Rows are numbered from 1 to N from top to bottom and columns are numbered from 1 to M as we move from left to right. 

The seat at the intersection of the i−th row and j−th column is occupied if matrix[i][j]=1, otherwise it is empty. 


Distance between 2 seats is the Manhattan Distance of the 2 points in the 2D matrix. 

The couple needs wants to sit as close to each other as possible. What is the minimum manhattan distance between such empty pair of seats. If it is not possible, output -1.

Input: 
The first line contains T, the number of test cases. 
In each test case, the first line contains two integers n and m (1 ≤ m, n ≤ 106), number of rows and number of columns of matrices respectively. Note that sum of n×m across all test cases is ≤ 106.

The next n lines each contain m integers separated by spaces describing the state of occupancy of seats in the workspace.

Constraints:
 1≤T≤103 
 1≤N≤106 
 1≤M≤106 
 1≤Sum of N∗M over all test cases≤106 

Output Format:
Output the minimum distance between two empty seats if possible. Otherwise, print -1."""


def Manhattan_distance(x,y,n):
    distance_array=[]
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            sum=abs(x[i]-x[j])+abs(y[i]-y[j])
            distance_array.append(sum)
    print(min(distance_array))

t=int(input())
while t!=0:
    n,m=list(map(int,input().split()))
    classroom=[]
    for i in range(n):
        row=list(map(int,input().split()))
        classroom.append(row)
    x=[]
    y=[]
    n_of_nodes=0
    for i in range(n):
        for j in range(m):
            if classroom[i][j]==0:
                n_of_nodes+=1
                x.append(i)
                y.append(j)

    if n_of_nodes==0 or n_of_nodes==1:
        print(-1)
    else:
        Manhattan_distance(x,y,n_of_nodes)
    t-=1
    
    
"""
Input :

2
8 4
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 0 1 1 
1 1 0 1 
1 1 1 1 
1 1 1 1 
7 6
1 0 0 1 1 0 
1 1 1 1 1 1 
0 1 1 0 1 1 
1 1 1 1 1 1 
1 0 1 0 1 1 
1 1 1 1 1 1 
1 1 1 1 1 1
"""

"""
Output:
2
1
"""
