class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        prereqHash = {i:[] for i in range(numCourses)}
        for edge in prerequisites:
            prereqHash[edge[0]].append(edge[1])
        
        visited = set()
        visiting = set()
        res = []
        
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in prereqHash[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if course in visited:
                continue
            if not dfs(course):
                return []
            
        return res
        