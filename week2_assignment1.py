t=int(input())              #number of test cases
while(t!=0):
    count=0
    n,x=list(map(int,input().split()))              #inputting the number of people and must be taller than the jth person in first row
    h = [int (h) for h in input().split()]          #inputting the heights of 2N people
    h.sort()
    firstrow=h[:n]
    secondrow=h[n:]
    for j in range(n):
        if((secondrow[j]-firstrow[j])>=x):
            count+=1
        else:
            count=0
            break
    if(count==n):
        print("YES")
    else:
        print("NO")
    t-=1
