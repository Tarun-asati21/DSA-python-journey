class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # convert the adjacency matrix into adjacency list :
        matrix = collections.defaultdict(list)
        r, c = len(isConnected), len(isConnected[0])
        for i in range(r):
            for j in range(c):
                if isConnected[i][j]==1 and i!=j : # !i=j assures that there is no self loop edge
                    matrix[i].append(j)
                    matrix[j].append(i)

        visited=[0]*r
        def dfs(start):
            visited[start]=1
            for n in matrix[start]:
                if visited[n]==0:
                    dfs(n)

        count=0
        for i in range(r) :
            if visited[i] == 0 :
                dfs(i)
                count+=1
        return count