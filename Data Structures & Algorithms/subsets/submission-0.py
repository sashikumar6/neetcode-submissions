class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        temp=[]

        def dfs(i):
            if i >= n:
                res.append(temp.copy())
                return 
            
            dfs(i+1)

            temp.append(nums[i])
            dfs(i+1)
            temp.pop()

        dfs(0)
        return res