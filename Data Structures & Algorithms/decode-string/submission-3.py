class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        num=0
        cur=""

        for i in s:

            if i.isdigit():
                num=num*10+int(i)
            
            elif i =="[":
                stack.append([cur,num])
                cur=""
                num=0
            elif i=="]":
                prev,k=stack.pop()
                cur=prev+cur*k
            else:
                cur+=i
        
        return cur
                
                