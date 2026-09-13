class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        def manhattan(x1,x2,y1,y2) :
            return abs(x1-x2)+abs(y1-y2)

        reachable = {}
        count=0
        for row in drones :
            limit = row[-1]
            max_dist = manhattan(row[0],target[0],row[1],target[1])
            if max_dist <= limit :
                reachable[count] = max_dist
            count+=1

        if reachable == {} :
            return -1

        sorted_freq = dict(sorted(reachable.items(), key = lambda items : (items[1],items[0])))
        for key in sorted_freq.keys():
            return key