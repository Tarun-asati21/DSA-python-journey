class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(idx, subset):
            if idx >= n*2 :
                result.append("".join(subset))
                return

            subset.append("(")
            backtrack(idx+1, subset)
            subset.pop()

            subset.append(")")
            backtrack(idx+1, subset)
            subset.pop()

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

        backtrack(0,[])
        ans = []
        for res in result :
            if valid(res) == True :
                ans.append(res)
        return ans 