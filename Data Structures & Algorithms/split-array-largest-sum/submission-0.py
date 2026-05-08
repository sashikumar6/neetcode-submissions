class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum):
            cur_sum=0
            count=1

            for i in nums:
                if cur_sum+i > max_sum:
                    cur_sum=i
                    count+=1
                else:
                    cur_sum+=i
            
            return count<=k
        
        left=max(nums)
        right=sum(nums)

        while(left<right):
            mid=(left+right)//2
            if canSplit(mid):
                right=mid
            else:
                left=mid+1

        return left