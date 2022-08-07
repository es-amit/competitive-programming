t=int(input())   #test cases
while(t!=0):
    n,q = list(map(int,input().split()))            #inputting the number of boxes and queries
    a = [int(a) for a in input().split()]           #boxes have number of Maggis
    a.sort(reverse=True)                            #Ulti krdo maggie ki list ko
    for i in range(q):
        x=int(input())                              #inputting one by one queries
        maggiessum = a[0]                           #maggiesum ko 1st element se initailise krenge
        packets=1                                   #toh fir hume uske liye 1 packet bhi chahiye hoga
        if(sum(a)<x):                               #agar a list ka sum query se chota hai toh -1 print krdo
            print(-1)
        else:
            for j in range(n):                      #nhi toh n tk loop chlegi
                if(maggiessum<x):                   #agar maggiesum chota query se toh
                    maggiessum+=a[j+1]              #maggiesum me add krdo number of maggie ka jo agle wala element hai
                    packets+=1                      #aur packet me bhi ek plus kr do
            print(packets)
    t-=1
