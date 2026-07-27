class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        sub=set()
        ans=float("-inf")
        for r in range(len(s)):
            
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            
            sub.add(s[r])
            
            ans=max(ans,r-l+1)
        
        return ans
