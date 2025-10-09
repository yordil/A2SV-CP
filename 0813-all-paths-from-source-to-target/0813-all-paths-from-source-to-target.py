class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        queue = deque([(0, [0])])  
        ans = []

        while queue:
            node, path = queue.popleft()

            if node == target:
                ans.append(path)
                continue

            for nbr in graph[node]:
                queue.append((nbr, path + [nbr]))  

        return ans