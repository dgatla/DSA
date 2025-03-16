from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacency_list = defaultdict(list)

        for course_a, course_b in prerequisites:
            adjacency_list[course_a].append(course_b)
        
        is_prerequisite = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        
        for i in range(numCourses):
            queue = deque([i])

            while queue:
                node = queue.popleft()
                
                for neighbours in adjacency_list[node]:
                    if not is_prerequisite[node][neighbours]:
                        queue.append(neighbours)
                        is_prerequisite[node][neighbours] = True
                    
                
        ans = []
        for course_a, course_b in queries:
            ans.append(is_prerequisite[course_a][course_b])
        
        return ans
        