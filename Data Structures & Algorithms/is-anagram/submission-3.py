class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount=[0]*26
        tCount=[0]*26

        for i in s:
            sCount[ord(i)-ord('a')]+=1
        
        for i in t:
            tCount[ord(i)-ord('a')]+=1

        
        
        return True if sCount==tCount else False
        