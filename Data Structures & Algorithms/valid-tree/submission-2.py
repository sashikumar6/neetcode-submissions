class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit=set()
        cycle=set()
        adj={i:[] for i in range(n)}

        if not n:
            return True

        for cur, neighbor in edges:
            adj[cur].append(neighbor)
            adj[neighbor].append(cur)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor==prev:
                    continue
                if dfs(neighbor,node) ==False:
                    return False
                  
            return True

        return dfs(0,-1) and len(visit) == n

