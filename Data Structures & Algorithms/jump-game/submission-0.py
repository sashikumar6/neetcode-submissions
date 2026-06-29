class Solution:
    def canJump(self, nums: List[int]) -> bool:
        new_pos=0
        farthest=0

        for i in range(len(nums)):
            if i>farthest:
                return False

            new_pos=i+nums[i]

            farthest=max(farthest,new_pos)

            if farthest>=len(nums)-1:
                return True
            
        return True