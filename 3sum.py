class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        sum=10**99
        for i in range(len(A)):
            x=i+1
            y=len(A)-1
            while x<y:
                s=A[i]+A[x]+A[y]
				
                if abs(B-s)<abs(B-sum):
                    sum=s
					
                if s>B:
                    y-=1
                else:
                    x+=1
        return sum