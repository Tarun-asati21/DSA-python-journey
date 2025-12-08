class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        # brute force : TLE 
        # sumi=sum(nums)
        # length=len(nums)
        # if sumi <= threshold :
        #     return 1
        # elif len(nums)==threshold:
        #     return max(nums)
        # else :
        #     for i in range (2, max(nums))  :
        #         sumi = 0
        #         for num in nums :
        #             sumi += (num+i-1) // i
        #         if sumi <= threshold :
        #             return i 

        # binary search
        nums.sort()
        low = 1
        high = max(nums)
        mini = float("inf")
        while low <= high:
            mid = (low + high) // 2
            sumi = 0
            for num in nums:
                sumi += (num + mid - 1) // mid  # ceiling value
            
            if sumi <= threshold:      # ignore right half
                mini = mid           
                high = mid - 1
            else:                   # ignore left half
                low = mid + 1
        return mini