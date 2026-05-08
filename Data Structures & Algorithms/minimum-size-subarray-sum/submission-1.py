class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sumval=0
        min_len=float("inf")
        
        for r in range(len(nums)):
            sumval+=nums[r]

            while sumval>=target:
                min_len=min(min_len,r-l+1)
                sumval-=nums[l]
                l+=1
        return 0 if min_len == float("inf") else  min_len