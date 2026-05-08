class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)

        length=max(m,n)
        res=''

        for i in range(length):
            if i<m:
                res+=word1[i]
            
            if i<n:
                res+=word2[i]
            
        return res
