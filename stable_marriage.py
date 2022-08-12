t = int(input())
while (t != 0):
    n = int(input())                                                #inputting the number of people
    marriages= []                                                   #initially taking there is no marriage so list is empty
    for i in range(n):
        marriages.append(-1)
    men=[]
    women=[]
    for i in range(n):
        p1=list(map(int,input().split()))                           #inputting into a variable
        p1.pop(0)                                                   #removing the first element because it gives us information about the precedence of a person
        women.append(p1)                                            #appending the precedence into list

    for i in range(n):
        p1=list(map(int,input().split()))
        p1.pop(0)
        men.append(p1)

    #initially all men are free
    freemen=[]
    propsal=[]
    for i in range(n):
        freemen.append(i+1)                                         #appending all the number of male into freemen list
    for i in range(n):
        propsal.append(0)                                           #initally there is no proposed to anyone
    while(len(freemen)>0):
        man = freemen.pop()
        proposeto=men[man-1][propsal[man-1]]
        propsal[man-1]+=1
        ind=proposeto-1
        if(marriages[ind]==-1):
            marriages[ind]=man
        elif (women[ind].index(marriages[ind]) < women[ind].index(man)):
            freemen.insert(len(freemen),man)
        else:
            oldhubby = marriages[ind]
            marriages[ind] = man
            freemen.insert(len(freemen),oldhubby)
        for i in range(n):
            print(i + 1,marriages[i])
    t -= 1
