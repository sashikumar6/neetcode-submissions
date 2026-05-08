class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for i in operations:
            if i == '+':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b)
                stack.append(a)
                stack.append(a+b)
            elif i== 'C':
                a=stack.pop()
            elif i=='D':
                a=int(stack.pop())
                stack.append(a)
                stack.append(2*a)
            else:
                stack.append(int(i))
        return sum(stack)
               