class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # brtue force approach -> TC = O((m+n).(log(m+n)))
        def med(arr):
            n = len(arr)
            if n == 0:
                return 0  
            if n % 2 == 0:
                return (arr[n//2 - 1] + arr[n//2]) / 2
            else:
                return arr[n//2]

        nums = nums1+nums2
        nums.sort()
        return med(nums)
    