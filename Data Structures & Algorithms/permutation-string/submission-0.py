class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        Count1=Counter(s1)
        l=0
        r=len(s1)

        while(r<len(s2)+1):
            Count2=Counter(s2[l:r])
            if Count1==Count2:
                return True
            l+=1
            r+=1
        
        return False
    