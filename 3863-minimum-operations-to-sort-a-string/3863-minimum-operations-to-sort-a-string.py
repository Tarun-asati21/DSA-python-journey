class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Case 1: Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Case 2: Cannot sort an unsorted string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Case 3: One operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Case 4: An extreme character is in the middle
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Case 5: Both extremes are on the wrong ends
        return 3
