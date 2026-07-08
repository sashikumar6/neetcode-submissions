class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count=Counter(nums)

        heap=[]

        for i, freq in count.items():
            heapq.heappush(heap,(-freq,i))
        

        while k>0:
            freq,value=heapq.heappop(heap)
            ans.append(value)
            k-=1
        
        return ans

        

