from __future__ import print_function
st,r=raw_input().split()
r=int(r)
n=len(st)
if(r==0):
      print(st)
elif(r==len(st)):
      print("")
else:      
      min_index=st.index(min(st))
      newr=r-(min_index)
      newst=st[min_index:]
      newlst=list()
      for i in newst:
            newlst.append(i)
      newlst.sort()
      if(newr>0):
            for i in range(newr):
                  newlst.pop()
      for i in newlst:
            print(i,end="")






##def smallestnumber(st,n,res):
##      if(n==0):
##            res.append(st)
##            return
##      if(n==len(st)):
##            return
##      else:
##            min_index=st.index(min(st))
##            res=st[min_index]
##            newstr=st[min_index:]
##            smallestnumber(newstr,n-min_index,res)
##                  
##
##st,n=raw_input().split()
##n=int(n)
##res=""
##print(smallestnumber(st,n,res))
##


##st=map(int,raw_input())
##n=len(st)
##r=int(raw_input())
##st.sort()
##p=n-r
##print(st[0:p])

