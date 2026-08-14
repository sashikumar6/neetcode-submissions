class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={')':'(','}':'{',']':'['}
        stack=[]


        for i in s:
            if i in hashMap:
                if not stack or stack[-1]!=hashMap[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        print(stack)
            
        if stack:
            return False
        else:
            return True


            
                