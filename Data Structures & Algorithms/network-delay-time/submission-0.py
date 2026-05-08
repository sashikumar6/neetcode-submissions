class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minheap=[(0,k)]
        visited=set()
        t=0

        while minheap:
            weight1,node1=heapq.heappop(minheap)

            if node1 in visited:
                continue
            visited.add(node1)
            t=max(t,weight1)

            for node2,weight2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minheap,(weight1+weight2,node2))
        
        if len(visited)==n:
            return t
        else:
            return -1 


