class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = [0] * numCourses
        # 0 = unvisited
        # 1 = currently visiting
        # 2 = completely visited

        def dfs(course):
            if visited[course] == 1:
                return False  # Cycle found

            if visited[course] == 2:
                return True   # Already processed

            visited[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visited[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True