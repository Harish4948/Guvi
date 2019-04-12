n=int(raw_input())
l=map(int,raw_input().split()) #get the numbers
d=dict()    # store the occurances

for i in l:
      if i not in d.keys(): #unique elements
            d.update({i:1})
            if(l.index(i)==n-1):
                  print("unique")
      else:
            print(i)
            break
      
            #update the occurance
##            
##            k=d[i]
##            d[i]=k+1
##un=list() # To store unique elements with Occurane 1
##for i in l:
##      if(d[i]==1):
##            un.append(i)
##for i in un:
##      print(i),
##            
##            
