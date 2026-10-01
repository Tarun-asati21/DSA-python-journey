class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        n = len(candidates)

        def backtrack(idx, total, subset):
            if total == 0 :
                result.append(subset.copy())
                return 
            if total < 0 :
                return 

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1] :
                    # if next element same as previosu choosen element for same position, then skip
                    continue

                remaining = total - candidates[i]
                subset.append(candidates[i])
                backtrack(i+1, remaining, subset)

                # backtracking
                subset.pop()

        backtrack(0, target, [])
        return result
            