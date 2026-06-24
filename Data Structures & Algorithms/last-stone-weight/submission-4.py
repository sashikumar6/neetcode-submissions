class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]

        for i in stones:
            heap.append(-i)
        
        heapq.heapify(heap)


        while len(heap)>1:

            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)

            diff = x - y

            heapq.heappush(heap,-diff)
        

        if not heap:
            return 0
        
        return -heap[0]


