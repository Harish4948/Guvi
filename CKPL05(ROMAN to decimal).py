def value(n):
      if(n=="I"):
            return 1
      if(n=="V"):
            return 5
      if(n=="X"):
            return 10
      if(n=="L"):
            return 50
      if(n=="C"):
            return 100
      if(n=="D"):
            return 500
      if(n=="M"):
            return 1000
      return -1

def con(n):
      res=0
      i=0

      while(i<len(n)):
            n1=value(n[i])
            if(i+1<len(n)):
                  n2=value(n[i+1])

                  if n1>=n2:
                        res=res+n1
                        i=i+1
                  else:
                        res=res+(n2-n1)
                        i=i+2
            else:
                  res=res+n1
                  i=i+1
      return res
n=raw_input()
print(con(n))
                  
