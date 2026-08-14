class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        def isAlphanumeric(t):
            return (
                (ord('a')<=ord(t)<=ord('z')) or
                (ord('A')<=ord(t)<=ord('Z')) or 
                (ord('0')<=ord(t)<=ord('9'))
            )

        while l<r:
            print(s[l],s[r])

            while l<r and not isAlphanumeric(s[l]):
                l+=1
            
            while l<r and not isAlphanumeric(s[r]):
                r-=1
            
            print(s[l],s[r])
            if s[l].lower()!=s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True
        
        
            







            
                    


