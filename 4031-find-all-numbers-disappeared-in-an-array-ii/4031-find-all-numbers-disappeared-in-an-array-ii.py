class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        req_lst = []
        for i in range(lower, upper+1) :
            req_lst.append(i)

        missing = sorted(list(set(req_lst) - set(nums)))

        if not missing :
            return []

        ranges = []
        start = missing[0]
        end = missing[0]

        # Runs only if len(nums) > 1
        for i in range(1, len(missing)):
            if missing[i] == end + 1:
                end = missing[i]
            else:
                ranges.append([start, end])
                start = missing[i]
                end = missing[i]

        # Captures the range for len(nums) == 1 or the final range
        ranges.append([start, end])

        return ranges

        