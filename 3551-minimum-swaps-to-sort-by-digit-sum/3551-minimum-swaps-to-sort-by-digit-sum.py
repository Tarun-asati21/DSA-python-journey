class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(n):
            return sum(int(digit) for digit in str(n))

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        val_to_target_idx = {val: idx for idx, val in enumerate(sorted_nums)}
        visited = [False] * n
        swaps = 0

        # Outer Loop: The Search Party (looks for new independent cycles)
        for i in range(n):
            # If this index is already visited or already in the correct place, skip it
            if visited[i] or val_to_target_idx[nums[i]] == i:
                continue

            # Inner Loop: Walk around the specific circle (cycle)
            cycle_size = 0
            current = i
            while not visited[current]:
                visited[current] = True
                # Jump to the next position in the loop
                current = val_to_target_idx[nums[current]]
                cycle_size += 1

            # A cycle of size k requires (k - 1) swaps to fix
            if cycle_size >= 1:
                swaps += cycle_size - 1

        return swaps    