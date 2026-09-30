class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(idx, subset, total):
            if idx >= n*2 :
                if total == 0 :
                    result.append("".join(subset))
                return
            elif total < 0 :
                return
            subset.append("(")
            total += 1
            backtrack(idx+1, subset, total)
            subset.pop()
            total -=1

            subset.append(")")
            total -= 1
            backtrack(idx+1, subset, total)
            subset.pop()
            total-=1

        backtrack(0,[],0)
        return result