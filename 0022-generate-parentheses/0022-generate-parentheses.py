class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(idx, subset, total):
            if idx >= n*2 :
                if total == 0 and subset[0] == "(" and subset[-1] == ")":
                    result.append("".join(subset))
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

        def valid(paranthesis) :
            stack = []
            for ch in paranthesis :
                if ch == "(" :
                    stack.append(ch)
                else :
                    if len(stack) == 0 :
                        return False
                    stack.pop()
            
            return len(stack) == 0

        backtrack(0,[],0)
        ans = []
        for res in result :
            if valid(res) == True :
                ans.append(res)
        return ans