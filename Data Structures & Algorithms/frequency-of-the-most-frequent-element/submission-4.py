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

'''
Sort the array so the largest value in any window is at the right end (nums[r]).

 Use a sliding window [l..r] and keep the sum of the window (total).

 Cost to make every element equal to nums[r] is
nums[r] * window_size - total.

If cost > k, move l right (shrink window); otherwise update the max window size.
'''