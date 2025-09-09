class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def initial_check(nums) :
            index = 1
            length = len(nums)
            while index < length :
                if nums[index] < nums[index-1] :
                    return False, index 
                index+=1
            return True
        
        if initial_check(nums)== True :
            return True
        if initial_check(nums)[0] == False :

            d = initial_check(nums)[1] # no of rotations

            arr_1 = nums[0:d]
            arr_2 = nums[d:]
            arr_3 = arr_2 + arr_1

            if initial_check(arr_3) == True :
                return True
            if initial_check(arr_3)[0] == False :
                return False

