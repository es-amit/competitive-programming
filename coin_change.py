n=int(input())
bills=0
coin=[100,20,10,5,1]
i=0
while(n!=0):
    if(coin[i]<=n):
        bills += n//coin[i]
        n = n%coin[i]

    else:
        i+=1
print(bills)
