x,y=list(map(str,raw_input().split()))
l1,l2=len(x),len(y)
if  l2>l1:
    i=0
    while(i<l1 and x[i]==y[i]):
        i+=1
    print(l2-i)
elif(l2==l2 or l1>l2):
    i=0
    while i<l2 and x[i]==y[i]:
        i+=1
    print(l1-i)
    
