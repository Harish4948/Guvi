n=raw_input()
l=map(int,raw_input().split())
s=abs(l[0]+l[1])
if s==0:
      print(l[0]),
      print(l[1])

for i,v in enumerate(l):
      for j in range(i+1,len(l)):
            temp=[l[i],l[j]]
            res=abs(temp[0]+temp[1])
            if res<=s:
                  s=res
                  x,y=l[i],l[j]
                  if s==0:
                        print(x),
                        print(y)
                        break
print(x),
print(y)
