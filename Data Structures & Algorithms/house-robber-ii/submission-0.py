class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        

        def rob_linear(arr):
            n=len(arr)
            
            if n==0:
                return 0
            
            if n==1:
                return arr[0]
            
            best=[0]*n
            best[0]=arr[0]
            best[1]=max(arr[0],arr[1])

            for i in range(2,len(arr)):
                best[i]=max(best[i-1],arr[i]+best[i-2])
            
            return best[-1]
        

        if n==0:
            return 0
        if n==1:
            return nums[0]

        res=0
        res=max(rob_linear(nums[0:n-1]),rob_linear(nums[1:n]))
        return res