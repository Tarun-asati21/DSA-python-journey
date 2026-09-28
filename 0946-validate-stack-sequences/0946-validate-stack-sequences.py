class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        count = 0
        
        for val in pushed:
            stack.append(val)
            # Pop matching elements as long as top matches popped[count]
            while stack and count < len(popped) and stack[-1] == popped[count]:
                stack.pop()
                count += 1
                
        # If all elements were successfully popped, stack will be empty
        return len(stack) == 0