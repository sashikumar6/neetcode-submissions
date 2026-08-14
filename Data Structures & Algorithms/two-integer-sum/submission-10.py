class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}

        for index,value in enumerate(nums): #0,3, 1,4
            need = target - value #4 3

            if need in hashMap:
                return [hashMap[need],index]

            hashMap[value]=index #{3:0}
            
          
            
        