class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1=nums[:n]
        nums2=nums[n:]
        lst=[]
        for i in range (0, len(nums1)):
            lst.append(nums1[i])
            lst.append(nums2[i])
        return lst