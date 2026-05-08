class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r #worst case result would be maximum of pile

        while l<=r:
            hours=0

            k=(l+r)//2

            for i in piles:
                hours+= math.ceil(i/k)

            if hours>h:
                l=k+1
            else:
                res=min(res,k)
                r=k-1
                    
        return res
    


    
                
                

