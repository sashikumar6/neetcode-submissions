class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        stack=[]
        
        for i in asteroids:
            alive = True

            while alive and stack and stack[-1]>0 and i <0:
                top = stack[-1]

                if abs(top)>abs(i):
                    alive = False
                elif abs(top)== abs(i):
                    stack.pop()
                    alive = False
                else:
                    stack.pop()
            
            if alive:
                stack.append(i)
        
        return stack

                