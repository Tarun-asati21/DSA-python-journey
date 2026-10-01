class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        balance = 0
        for ch in s :
            if ch in ["(","{","["] :
                stack.append(ch)
                balance += 1
                continue
            if balance <= 0 :
                return False
            elif ch == "}" :
                check = stack[-1]
                if check != "{" :
                    return False
                stack.pop()
                balance -= 1
            elif ch == ")" :
                check = stack[-1]
                if check != "(":
                    return False
                stack.pop()
                balance -= 1
            elif ch == "]":
                check = stack[-1]
                if check != "[":
                    return False
                stack.pop()
                balance -= 1
        return len(stack)==0