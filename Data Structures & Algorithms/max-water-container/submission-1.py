class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        best=0

        while l<r:
            length=r-l
            
            area=length*(min(height[l],height[r]))
            
            if height[l]>height[r]:
                r=r-1
            else:
                l+=1
            if area > best:
                best=area
        return best