class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[]

        for i in count.values():
            heapq.heappush(heap,-i)
        
        time=0
        q=deque()
        while heap or q:
            time+=1

            if heap:
                cnt=heapq.heappop(heap)+1
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                tsk=q.popleft()[0]
                heapq.heappush(heap,tsk)
        
        return time




