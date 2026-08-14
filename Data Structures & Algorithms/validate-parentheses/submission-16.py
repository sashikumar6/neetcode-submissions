class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={')':'(','}':'{',']':'['}
        stack=[]


        for i in s:
            if i in hashMap:
                if stack and stack[-1]==hashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        print(stack)
            
        if stack:
            return False
        else:
            return True


            
                