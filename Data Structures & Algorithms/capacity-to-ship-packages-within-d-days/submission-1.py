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
        
        l=max(weights)
        r=sum(weights)

        while l<=r:
            mid=(l+r)//2

            if canShip(mid):
                r=mid-1
            else:
                l=mid+1
            
        return l



#goal is to get minimum capacity, so even if we find value on first iteration we keep trying for smaller capacity.  
#helper function give us, if we can do in the given days with that capacity
# if yes, we make the capacity into half and try again        