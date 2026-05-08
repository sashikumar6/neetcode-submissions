class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for index, value in enumerate(temperatures):
            while stack and value>stack[-1][1]:
                prev_index,prev_value  = stack.pop()
                res[prev_index]=index-prev_index
            
            stack.append([index,value])
        
        return res


        