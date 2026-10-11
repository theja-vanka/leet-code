class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        pre_req = {i: [] for i in range(numCourses)}

        for s, e in prerequisites:
            pre_req[s].append(e)
        
        visit = set()

        def dfs(crs):
            if crs in visit: return False

            if not pre_req[crs]:
                return True
            
            visit.add(crs)
            for c in pre_req[crs]:
                if not dfs(c): return False
            
            visit.remove(crs)
            pre_req[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True