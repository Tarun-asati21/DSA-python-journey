import collections

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        # convert the input into adjacency list
        graph = collections.defaultdict(list)
        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)

        # bfs - approach
        queue = collections.deque()
        visited = [0]*(n)
        queue.append(source)

        while len(queue)!=0:
            node = queue.popleft()
            if node == destination :
                return True
            for vertex in graph[node] :
                if visited[vertex] == 0 :
                    queue.append(vertex)
                    visited[vertex] = 1 
        return False