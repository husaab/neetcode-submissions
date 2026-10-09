class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # storing course -> prereq is the best option

        prerequisites_map = {}

        for course, prereq in prerequisites:
            prerequisites_map.setdefault(course, []).append(prereq)

        visited = set()
        completed = set()
        def dfs(course, visited):
            if course in visited:
                return False
            
            if course in completed:
                return True

            visited.add(course)
            
            for prereq in prerequisites_map.get(course, []):
                if not dfs(prereq, visited):
                    return False

            visited.remove(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i, visited):
                return False
        
        return True
        