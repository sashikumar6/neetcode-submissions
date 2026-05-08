class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        out=0
        i=j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                out+=1
                i+=1
                j+=1
            else:
                j+=1
        return out

