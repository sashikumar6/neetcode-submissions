class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq=Counter(nums)

        heap=[]
        res=[]

        for value,count in freq.items():

            heapq.heappush(heap,(count,value))

            if len(heap)>k:
                heapq.heappop(heap)
        
        for count,num in heap:
            res.append(num)
        
        return res

