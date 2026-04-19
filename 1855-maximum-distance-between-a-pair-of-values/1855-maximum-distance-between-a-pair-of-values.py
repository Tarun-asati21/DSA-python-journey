class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force with iteration pruning - TLE
        # if nums1[-1] > nums2[0] :
        #     return 0 
        # maxi = -float("inf")
        # for i in range (0, len(nums1)):
        #     for j in range(i, len(nums2)):
        #         if nums1[i] > nums2[j] :
        #             break 
        #         else :
        #             dist = j-i
        #             maxi = max(maxi, dist)
        # return 0 if maxi == -float("inf") else maxi 

        # two pointer approach 
        i, j = 0,0
        ans =0 

        while i < len(nums1) and j < len(nums2) :
            if nums1[i] <= nums2[j] :
                ans = max(ans, j-i)
                j+=1
            else :
                i += 1
                if i > j :
                    j=i
        return ans 