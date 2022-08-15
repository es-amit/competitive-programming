t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    f_turn="Ankita"
    #first line of output
    if(max(b)>max(a)):
        f_turn="Biswas"
    elif(max(b)<=max(a)):
        f_turn="Ankita"
    print(f_turn)


    #second line of output
    turn=[]
    a_max=max(a)
    b_max=max(b)
    turn.append(b_max)
    if(b_max < a_max):
        turn.append(a_max)
    if(len(turn)%2==0):
        print("Ankita")
    else:
        print("Biswas")
    t-=1
