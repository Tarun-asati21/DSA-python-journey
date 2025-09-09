class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # not inplace approach
        # lst=[]
        # index = 0
        # size = len(nums)
        # while index < size :
        #     if nums[index] != nums[index-1] :
        #         lst.append(nums[index])
        #     index += 1

        # expectedNums = lst
        # count = len(expectedNums)
        # return count


        # inplace approach -> two pointer approach
        i = 0
        for j in range (1,len(nums)):
            if nums[i] != nums[j] :
                nums[i+1] = nums[j]
                i += 1
        
        return i+1