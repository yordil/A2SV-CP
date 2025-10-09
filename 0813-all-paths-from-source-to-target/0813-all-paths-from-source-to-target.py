class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans   = []
        def dfs(node , path):
            if node == target:
                ans.append(path)
            for nbr in graph[node]:
                dfs(nbr , path + [nbr])

        dfs(0 , [0])


        return ans 