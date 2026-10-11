class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        visit, cycle = set(), set()
        pre_req = {i: [] for i in range(numCourses)}
        output = []

        for s, e in prerequisites:
            pre_req[s].append(e)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for c in pre_req[crs]:
                if not dfs(c): return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return output