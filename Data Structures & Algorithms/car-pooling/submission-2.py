class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips =sorted(trips, key=lambda x: x[1])

        heap=[]
        curr_pass=0

        for passenger, start, end in trips:
            while heap and heap[0][0] <= start:

                drop_loc, old_pass = heapq.heappop(heap)

                curr_pass -=old_pass
            
            curr_pass+=passenger

            if curr_pass > capacity:
                return False
            
            heapq.heappush(heap, (end, passenger))

        return True
