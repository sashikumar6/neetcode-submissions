class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        def is_pali(i,j):
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return is_pali(i+1,j) or is_pali(i,j-1)

        return True
