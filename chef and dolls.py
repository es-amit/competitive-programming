t=int(input())
while(t!=0):
    a=[]
    n=int(input())
    for i in range(n):
        item=int(input())
        a.append(item)
    for i in a:
        count=a.count(i)
        if(count%2!=0):
            miss=i
            break
    print(miss)
    t-=1
