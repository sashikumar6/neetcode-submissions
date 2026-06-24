import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        n = len(stones)

        while True:
            if stones:
                item1 = -1*heapq.heappop(stones)
            else:
                return 0
            if stones:
                item2 = -1*heapq.heappop(stones)
            else:
                return item1

            item_new = item1 - item2

            if item_new != 0:
                heapq.heappush(stones, -item_new)
        
