class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # brute force :
        mini = float("inf")
        for i in range (len(nums)) :
            if nums[i] == target :
                dist = abs(i-start)
                mini = min(dist, mini)
        return mini