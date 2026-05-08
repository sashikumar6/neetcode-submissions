class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for index,value in enumerate(nums):
            if index>0 and value==nums[index-1]:
                continue
            l=index+1
            r=len(nums)-1
            while l<r:
                summ=value+nums[l]+nums[r]
                if summ >0:
                    r-=1
                elif summ<0:
                    l+=1
                else:
                    res.append([value,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

