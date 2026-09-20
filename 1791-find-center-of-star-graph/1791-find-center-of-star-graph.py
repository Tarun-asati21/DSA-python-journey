class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # array brute force coming to my mind is at first instant :
        # arr = edges[0]  + edges[1]
        # freq={}
        # for num in arr :
        #     freq[num] = freq.get(num,0)+1
        # for k,v in freq.items() :
        #     if v == 2 :
        #         return k

        # using graph theory - degree concept :
        # the center node since is connected to every other node :  N-1 edges , ie degree = N-1
        degree = {}
        for edge in edges :
            node1 = edge[0]
            node2 = edge[1]
            degree[node1] = degree.get(node1,0)+1
            degree[node2] = degree.get(node2,0)+1
        
        for k,v in degree.items():
            if v == len(edges) :
                return k


