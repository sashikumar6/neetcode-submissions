class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if ((m-1<0 or nums[m-1] !=nums[m]) and 
            (m+1==len(nums) or nums[m] != nums[m+1])):
                return nums[m]
            
            if nums[m-1]==nums[m]:
                leftsize=m-1
            else:
                leftsize=m
            
            if leftsize%2==0:
                l=m+1
            else:
                r=m-1
            