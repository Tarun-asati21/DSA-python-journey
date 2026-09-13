class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s :
            if len(stack)==0 :
                stack.append(ch)
            else :
                last = stack[-1]
                if last=="{" and ch=="}" :
                    stack.pop()
                elif last=="[" and ch=="]" :
                    stack.pop()
                elif last=="(" and ch==")" :
                    stack.pop()
                else :
                    stack.append(ch)

        if len(stack) == 0 :
            return True
        else :
            return False