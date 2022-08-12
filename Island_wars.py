n, m = list(map(int, input().split()))
requests=[]
while(m != 0):
    request = tuple(map(int, input().split()))
    requests.append(request)
    m -= 1
requests.sort(key = lambda x: x[1])

ans=0
lastbridge=-1

for request in requests:
    if lastbridge > request[0]:
        continue
    else:
        lastbridge=request[1]
        ans+=1
print(ans)
