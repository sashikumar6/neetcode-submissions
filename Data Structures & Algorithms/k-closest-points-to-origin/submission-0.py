import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        dist=0

        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            
            dist=x*x + y*y

            heapq.heappush(heap,(-dist,x,y))

        while len(heap)>k:
            heapq.heappop(heap)

        res=[]
        for _,x,y in heap:

            res.append((x,y))
        
        return res
            