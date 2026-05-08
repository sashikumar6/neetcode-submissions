class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[l]

        while l<=r:
            if nums[l]<nums[r]:
                res=min(nums[l], res)
                break
            
            mid=(l+r)//2
            res=min(nums[mid],res)
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1

        return res            

        #We eliminate the sorted half that cannot contain the minimum.

        # if nums[mid]>nums[r]
        #mid is in the left (bigger) part
        #Right side contains smaller values
        #we move right

        #else --> move left
        