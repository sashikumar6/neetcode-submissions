class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in hashMap:
                if stack and hashMap[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append((i))
        
        if len(stack)==0:
            return True
        else:

            return False
