class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total < x :
            return -1
        if total == x:
            return n

        # Store prefix_sum -> number of operations from the left
        # prefix_map[0] = 0 means 0 elements picked from the left
        prefix_map = {0: 0}
        current_prefix = 0
        
        for i in range(n):
            current_prefix += nums[i]
            if current_prefix <= x:
                prefix_map[current_prefix] = i + 1
            else:
                break  # Stops early if prefix exceeds x

        min_ops = float('inf')

        # Check if taking ONLY prefix elements works
        if x in prefix_map:
            min_ops = min(min_ops, prefix_map[x])

        # Traverse suffix sums from the right and match with prefix map
        current_suffix = 0
        for j in range(n - 1, -1, -1):
            current_suffix += nums[j]
            suff_ops = n - j
            
            if current_suffix > x:
                break
                
            needed_prefix = x - current_suffix
            if needed_prefix in prefix_map:
                pre_ops = prefix_map[needed_prefix]
                
                # Ensure prefix and suffix bounds do not overlap
                if pre_ops + suff_ops <= n:
                    min_ops = min(min_ops, pre_ops + suff_ops)

        return min_ops if min_ops != float('inf') else -1