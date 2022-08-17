t=int(input())
while(t!=0):
    maxt,maxn,sumn=list(map(int,input().split()))
    n=0
    a=[]
    while(sumn!=0):
        sumn-=maxn
        n += 1
        a.append(maxn)
        if(n==maxt):
            break
        if(maxn>sumn):
            maxn=sumn
    iterations=0
    for i in range(len(a)):
        iterations+=a[i]**2
    print(iterations)
    t-=1
