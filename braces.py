
def braces(A):
   
   sign={'+','-','/'}
   dic={}
   for i in range(len(A)):
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
           
            if x==0:
               if s:
                  return 1
               dic[i]=j
               break
            j-=1
   
   return 0

s=input()
print(braces(s))
