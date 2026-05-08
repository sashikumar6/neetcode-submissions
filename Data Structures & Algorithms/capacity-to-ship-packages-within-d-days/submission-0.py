class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            cur=0
            days_used=1

            for w in weights:
                if cur+w<=capacity:
                    cur+=w
                else:
                    days_used+=1
                    cur=w
            
            return days_used<=days

        
        left=max(weights)
        right=sum(weights)

        while left<right:
            mid=(right+left)//2        

            if canShip(mid):
                right=mid
            else:
                left=mid+1

        return left            