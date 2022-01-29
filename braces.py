
class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        sign={'+','-','/','*'}
        dic={}
        for i in range(len(A)):
            if A[i]==')':   
                j=i-1
                s=True
                while j>-1:
                    if s and A[j] in sign:
                        s=False  
                    if A[j]==')':
                        j=dic[j]
                    elif A[j]=='(':
                        if s:
                            return 1
                        dic[i]=j
                        break
                    j-=1
        
        return 0
