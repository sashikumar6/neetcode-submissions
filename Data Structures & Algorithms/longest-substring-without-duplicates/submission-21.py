class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxlen=0

        l=0
        r=0

        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            r+=1
            maxlen=max(maxlen,len(seen))
        
        return maxlen
            
            

            



