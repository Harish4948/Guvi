n=raw_input()
l=map(int,raw_input().split())
op=list()
for i,v in enumerate(l):
      for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                  temp=[l[i],l[j],l[k]]
                  if(temp[0]+temp[1]==temp[2]):
                        
                        op.append(temp)
for i in range(len(op)):
      for j in range(3):
            print(op[i][j]),
      print("")


      
##      if(i+3<=len(l)):
##            temp=l[i:i+3]
##            print(temp)
##            if(len(temp)==3):
##                  if(temp[0]+temp[1]==temp[2]):
##                        op.append(temp)
##print(op)
##                        
