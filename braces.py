from collections import defaultdict
def braces(A):
   lc=-1
   sign={'+','-','/'}
   dic={}
   for i in range(len(A)):
      #print(i)   
      if A[i]==')':
         
            
         x=1
         j=i-1
         s=True
         while j>-1:
            if s and A[j] in sign:
               s=False
            if A[j]=='(':
               x-=1
            elif A[j]==')':
               j=dic[j]
            print(x,j)
            if x==0:
               if s:
                  return False
               dic[i]=j
               break
            j-=1
   print(dic)
   return True

s=input()
print(braces(s))
