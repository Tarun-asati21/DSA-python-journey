class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        mini = float("inf")
        for i, num in enumerate(nums):
            sumi = 0
            for ch in str(num) :
                sumi += int(ch)
            if sumi == i :
                mini = min(mini,i)
        return mini if mini != float("inf") else -1