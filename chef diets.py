t=int(input())
while(t!=0):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    extra=0
    for i in range(n):
        if(a[i]>k):
            extra+=a[i]-k
            flag=1
        elif(a[i]<k):
            a[i]+=extra
            if(a[i]<k):
                flag=0
                pos=i+1
                break
            else:
                extra=a[i]-k
                flag=1
        else:
            extra=0
            flag=1
    if(flag==1):
        print("YES")
    else:
        print(f"NO {pos}")

    t-=1
