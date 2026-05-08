import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)

        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)

            diff=x-y

            if diff>0:
                heapq.heappush(heap,-diff)
        if not heap:
            return 0
        return -heap[0]
        
