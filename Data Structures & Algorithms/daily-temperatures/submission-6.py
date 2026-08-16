class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]

        for index,value in enumerate(temperatures):
            while stack and stack[-1][1]<value:
                prev_index,prev_value = stack.pop()
                result[prev_index]=index-prev_index

            stack.append((index,value))
        
        return result
       
                

            
