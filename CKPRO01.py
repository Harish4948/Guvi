def longestprefix(s1,s2):
      n1=len(s1)
      n2=len(s2)
      result=""
      i=0
      j=0
      while(i<=n1-1 and j<=n2-1):
            if(s1[i]!=s2[j]):
                  break
            result=result+s1[i]
            i+=1
            j+=1
      return result
            

n=int(raw_input())
l=list()
for i in range(n):
      l.append(raw_input())
l.sort()
print(longestprefix(l[0],l[n-1]))
