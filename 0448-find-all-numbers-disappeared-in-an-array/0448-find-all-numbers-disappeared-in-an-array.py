class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        numbers = set(nums)
        ans = []
        for num in range(1, len(nums)+1):
            if num not in numbers:
                ans.append(num)
        return ans