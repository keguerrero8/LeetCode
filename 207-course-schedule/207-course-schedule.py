class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # [[1, 0], [1, 2], [2, 0]], {1:[0, 2], 2:[0], 3:[1]}
        prereqHash = {}
        for i in prerequisites:
            if i[0] not in prereqHash:
                prereqHash[i[0]] = [i[1]]
            else:
                prereqHash[i[0]].append(i[1])
                
        visiting = set()
        possibleCourses = set()
        
        for course in range(numCourses):
            isPossible = self.dFS(course, prereqHash, visiting, possibleCourses)
            if not isPossible:
                return False
            
        return True
    
    
    def dFS(self, course, prereqHash, visiting, possibleCourses):
        if course in visiting:
            return False
        
        if course not in prereqHash or course in possibleCourses:
            return True
        
        visiting.add(course)
        
        for prereq in prereqHash[course]:
            isPossible = self.dFS(prereq, prereqHash, visiting, possibleCourses)
            if not isPossible:
                return False
            
        possibleCourses.add(course)
        visiting.remove(course)
        
        return True
        
        
            
        
        