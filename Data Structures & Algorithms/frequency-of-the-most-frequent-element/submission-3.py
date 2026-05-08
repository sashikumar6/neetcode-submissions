class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        total=0
        ans=0
        nums.sort()
        for r in range(len(nums)):
            total+=nums[r]

            while nums[r] * (r-l+1) - total > k:
                total -=nums[l]
                l+=1
                
            ans=max(ans,r-l+1)
        
        return ans
