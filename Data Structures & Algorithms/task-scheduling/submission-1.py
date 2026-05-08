class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        cpucycle=0

        count=Counter(tasks)

        for i in count.values():
            heap.append(-i)
        heapq.heapify(heap)

        cooldown_q=deque()

        while cooldown_q or heap :
            cpucycle+=1

            if heap:
                current_count=heapq.heappop(heap)
                current_count+=1 # its in negative so +1 so reduce count
                
                if current_count:
                    cooldown_q.append([current_count, cpucycle+n] )
            
            if cooldown_q and cooldown_q[0][1]==cpucycle: # if current item in q, can be processed now
                cur_process_count=cooldown_q.popleft()[0]
                heapq.heappush(heap,cur_process_count) # remove from q, push to heap to process again because we need to process most freq elemt additing it to heap give as max freq letter
        
        return cpucycle
                