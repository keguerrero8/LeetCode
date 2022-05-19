class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dFS(course, prereqHash, visiting, canBeCompleted):
            if course not in visiting or visiting[course] == False:
                visiting[course] = True
            elif visiting[course] == True:
                return False
                
            if course not in prereqHash or course in canBeCompleted:
                visiting[course] = False
                return True
            
            for prereq in prereqHash[course]:
                isPossible = dFS(prereq, prereqHash, visiting, canBeCompleted)
                if not isPossible:
                    return False
                    
            canBeCompleted[course] = True      
            visiting[course] = False
                
            return True
        
        canBeCompleted = {}
        prereqHash = {}
        for prereq in prerequisites:
            if prereq[0] not in prereqHash:
                prereqHash[prereq[0]] = [prereq[1]]
            else:
                prereqHash[prereq[0]].append(prereq[1])
                
        visiting = {}
        isPossible = True
        
        for course in range(numCourses):
            isPossible = dFS(course, prereqHash, visiting, canBeCompleted)
            if not isPossible:
                return False
            canBeCompleted[course] = True
        
        return True
    
    