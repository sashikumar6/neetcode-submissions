class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        seen={}
        res=0

        for r in range(len(s)):

            if s[r] in seen:
                l=max(l,seen[s[r]]+1) #we move l to next to duplicate, basically skipping it
            seen[s[r]]=r

            res=max(res,r-l+1)
        
        return res


