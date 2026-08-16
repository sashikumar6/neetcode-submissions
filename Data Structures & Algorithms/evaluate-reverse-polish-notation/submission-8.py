class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={"+","-","*","/"}

        stack=[]

        for i in tokens:
            if i in operators:
                ops2=int(stack.pop())
                ops1=int(stack.pop())
                res=0

                if i == "+":
                    res=ops1+ops2
                elif i == "-":
                    res=ops1-ops2
                elif i == "*":
                    res=ops1*ops2
                elif i=="/":
                    res=ops1/ops2
            
                stack.append(res)

            else:
                stack.append(int(i))
        
        return int(stack[0])