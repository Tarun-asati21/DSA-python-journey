class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # brute force
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target :
                    return [i,j]

        # # better solution
        # i=0
        # for j in range(i+1, len(nums)):
        #     if nums[i]+nums[j]== target :
        #         return [i,j]
        #     elif nums[i]+nums[j] != target :
        #         if j == len(nums)-1 :
        #             i=i+1
        #         else :
        #             continue

            
