class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)

        if m>n:
            l=n
        else:
            l=m
        out=""
        for i in range(l):
            out+=word1[i]
            out+=word2[i]
        
        if l==m:
            out+=word2[l:n]
        else:
            out+=word1[l:m]

        return out