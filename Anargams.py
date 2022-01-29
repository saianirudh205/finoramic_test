from collections import defaultdict
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers

	def anagrams(self, A):
        dic=defaultdict(list)
        for s in range(len(A)):
            arr=[0]*26
            for j in A[s]:
                arr[ord(j)-ord('a')]+=1
            dic[str(arr)]+=[s+1]
        
        return list(dic.values())