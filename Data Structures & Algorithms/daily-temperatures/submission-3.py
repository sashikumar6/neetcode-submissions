class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex]=index-stackIndex
            
            stack.append([value,index])
        
        return res