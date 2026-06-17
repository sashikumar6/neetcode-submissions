class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet=set(nums)
        best=0
        if len(nums)==0:
            return 0  
        for i in numSet:
            if i-1 in numSet:
                continue

            length=1
            while i+length in numSet:
                length+=1   
            
            if length>best:
                best=length
    
        return best