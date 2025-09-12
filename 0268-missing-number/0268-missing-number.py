class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # better solution
        # lst=[]
        # n=len(nums)
        # for i in range (0,n+1) :
        #     lst.append(i)
        
        # missing_num = list(set(lst)-set(nums))
        # return missing_num[0]

        # optimal solution
        n=len(nums)
        expected_sum = n*(n+1)/2
        actual_sum = sum(nums)
        missing_no = expected_sum-actual_sum
        return missing_no