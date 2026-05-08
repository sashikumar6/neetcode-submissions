class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ansSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r]  in ansSet:
                ansSet.remove(s[l])
                l+=1
            
            ansSet.add(s[r])
            res=max(res,r-l+1)
        return res