n=raw_input()
l=map(int,raw_input().split())
op=[]
for i,v in enumerate(l):
      for j in range(i+1,len(l)):
            temp=[l[i],l[j]]
            res=temp[0]+temp[1]
            if(res>=0 and res<1):
                  op.append(temp)
for i in range(len(op)):
      for j in range(2):
            print(op[i][j]),
