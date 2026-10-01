class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        n=len(candidates)
        def backtrack(idx, total, subset) :
            if total == target :
                result.append(subset.copy())
                return
            if total > target or idx >= n :
                return
            
            # pick - same index
            sumi = total + candidates[idx]
            subset.append(candidates[idx])
            backtrack(idx, sumi, subset)

            # unpick - move to other index
            subset.pop()
            backtrack(idx+1, total, subset)

        backtrack(0, 0, [])
        return result
            