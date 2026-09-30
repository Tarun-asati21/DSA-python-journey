class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(start, remaining, subset):
            if remaining == 0:
                result.append(list(subset))
                return

            for i in range(start, len(candidates)):
                # Pruning: Skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning: Stop early if candidate exceeds remaining target
                if candidates[i] > remaining:
                    break

                subset.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], subset)
                subset.pop()

        backtrack(0, target, [])
        return result