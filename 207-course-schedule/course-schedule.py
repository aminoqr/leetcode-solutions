from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(course):
            state = states[course]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            
            states[course] = VISITING

            for nei in g[course]:
                if not dfs(nei):
                    return False
            
            states[course] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True