class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq={i:[] for i in range(numCourses)}
        visit=set()
        cycle=set()
        out=[]

        for crs,pre in prerequisites:
            preReq[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preReq[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            out.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) ==False:
                return []
        return out

        