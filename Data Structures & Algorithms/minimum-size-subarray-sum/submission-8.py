class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0

        summ=nums[0]
        ans=float("inf")
        while r<len(nums):
            
            if summ<target:
                r+=1
                if r < len(nums):
                    summ += nums[r]
                
            else:
                ans=min(ans,r-l+1)
                summ-=nums[l]
                l+=1


        if type(ans)!=int:     
            return 0 
        else:
            return ans   
            

