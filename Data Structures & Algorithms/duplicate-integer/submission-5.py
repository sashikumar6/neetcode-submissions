from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset=set(nums)

        if len(nums)== len(numset):
            return False
        else:
            return True
'''
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        if len(nums)==0:
            return False
        for key,value in freq.items():
            if 2 in freq.values():
                return True
            else:    
                return False 
            '''