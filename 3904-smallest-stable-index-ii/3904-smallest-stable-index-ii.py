class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # TC =  O(n) --> still TLE 
        # n = len(nums)
        # prefix_max=[nums[0]]
        # maxi = nums[0]
        # for i in range(1, n):
        #     maxi = max(maxi, nums[i])
        #     prefix_max.append(maxi)
        
        # suffix_min = [nums[-1]] 
        # mini = nums[-1]
        # for i in range(n-2, -1, -1) :
        #     mini = min(mini, nums[i])
        #     suffix_min.insert(0, mini)

        # for i in range(0, n) :
        #     if prefix_max[i] - suffix_min[i] <= k :
        #         return i 
        #         break
        # return -1
        
        # more good solution :
        n = len(nums)
        mini = [0] * n 

        mint = float("inf")
        for i in range(n-1, -1, -1 ) :
            if nums[i] < mint :
                mint = nums[i]
            mini[i] = mint
        
        maxi = 0
        for i in range(n):
            if nums[i] > maxi :
                maxi = nums[i]
            if maxi - mini[i] <= k :
                return i 
        return -1