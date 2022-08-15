t=int(input())
while(t!=0):
    passengers=0
    n,q=list(map(int,input().split()))
    s=[int(s) for s in input().split()]
    Q=[]
    for i in range(q):
        p1 = list(map(int,input().split()))
        Q.append(p1)

    for i in range(q):
        f_elem=Q[i][0]
        s_elem=Q[i][1]
        if((f_elem in s)and(s_elem in s)):
            f_ind=s.index(f_elem)
            try:
                s_ind=s.index(s_elem,f_ind)
                passengers+=1
            except:
                pass
    print(passengers)
    t-=1
