class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        result = []

        def backtrack(idx, total, subset) :
            if total == n and len(subset) == k :
                result.append(subset.copy())
                return 
            if total > n or idx >= 9 or len(subset) > k :
                return 

            # pick
            sumi = total + nums[idx]
            subset.append(nums[idx])
            backtrack(idx+1, sumi, subset)

            # not pick
            subset.pop()
            backtrack(idx+1, total, subset)

        backtrack(0,0,[])
        return result