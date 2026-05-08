class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pairs= sorted(zip(position,speed), reverse=True)

        slowest_time_ahead=0
        fleet=0

        for p,s in pairs:
            time= (target-p)/s

            if time > slowest_time_ahead:
                fleet+=1
                slowest_time_ahead=time
        
        return fleet


