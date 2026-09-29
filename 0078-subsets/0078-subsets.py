class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n=len(nums)
        def helper(idx, subset):
            if idx >= n :
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            helper(idx+1, subset)
            subset.pop()
            helper(idx+1, subset)

        helper(0,[])
        return result