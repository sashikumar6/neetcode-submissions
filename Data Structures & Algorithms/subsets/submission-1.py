class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        path=[]
        res=[]

        def dfs(i):
            if i >=n:
                res.append(path.copy()) #is the same list object throughout the recursion. storing reference
                return 
            
            dfs(i+1) #skip

            path.append(nums[i])
            dfs(i+1)
            path.pop()

        
        dfs(0)
        return res


