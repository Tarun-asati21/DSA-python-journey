class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # # brute force --> TLE 
        # maxi = -float("inf")
        # for i in range(0, len(nums) - k + 1):
        #     numerator = sum(nums[i : i + k])
        #     mean = round(numerator / k, 5)
        #     maxi = max(maxi, mean)
        # return maxi

        window_sum = sum(nums[:k])
        maxi = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i-k]    # remove previous element
            maxi = max(maxi, window_sum)
        
        return round(maxi / k,5)
