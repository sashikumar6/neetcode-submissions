class Solution:
    def isValid(self, s: str) -> bool:
        HashMap={')':'(', '}':'{',']':'['}
        stack=[]

        for i in s:
            if i in HashMap:
                if stack and stack[-1]==HashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return not stack
            
                