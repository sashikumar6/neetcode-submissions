class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
      
        n=len(nums)
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(temp[:])
                return
            
            if curr_sum > target or i ==n:
                return
            
            backtrack(i+1, curr_sum)

            temp.append(nums[i])
            backtrack(i, curr_sum+nums[i])
            temp.pop()
        
        backtrack(0,0)
        return res
            
            