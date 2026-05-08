class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        res=[]

        for point in points:

            x=point[0]
            y=point[1]

            distance=math.sqrt((x*x)+(y*y))

            heapq.heappush(heap,(distance,x,y))
        
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            
        
        return res