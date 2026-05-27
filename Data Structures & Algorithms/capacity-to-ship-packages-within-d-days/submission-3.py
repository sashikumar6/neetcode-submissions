class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def canShip(capacity):
            daysUsed=1
            cur=0

            for w in weights:
                if cur+w <= capacity:
                    cur+=w
                else:
                    daysUsed+=1
                    cur=w
            
            return daysUsed<=days
        
        l=max(weights)
        r=sum(weights)


        while l<=r:
            mid=(l+r)//2
            if canShip(mid):
                r=mid-1
            else:
                l=mid+1
        return l