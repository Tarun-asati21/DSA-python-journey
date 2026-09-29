class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        def helper(idx, subset):
            result.append(subset.copy())

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()

        helper(0, [])
        return result