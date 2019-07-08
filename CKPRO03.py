x,y=list(map(str,raw_input().split()))
l1,l2=len(x),len(y)
if  l2>l1:
    i=0
    while(i<l1 and x[i]==y[i]):
        i+=1
    print(l2-i)
elif(l2==l1):
    i=0
    while i<l2 and x[i]==y[i]:
        i+=1
    print(l1-i)
else:
    i=0
    while i<l2 and x[i]==y[i]:
        i+=1
    s31 = x[i:]
    s32 = y[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(l1-i-k)
