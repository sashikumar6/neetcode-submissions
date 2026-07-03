class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        res=[]

        for index,value in enumerate(nums):
            need=target-value

            if need in hashMap:
                return [hashMap[need],index]

            hashMap[value]=index
        return res



        