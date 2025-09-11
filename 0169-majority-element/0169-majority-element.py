class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # # brute force solution
        # # bubble sort
        # n= len(nums)
        # for i in range (n-1,0,-1):
        #     for j in range (0,i):
        #         if nums[j+1] < nums[j] :
        #             nums[j+1],nums[j]=nums[j],nums[j+1]
        
        # # counting frequency
        # count=1
        # for i in range(0,n):
        #     if count > n//2 :
        #         return nums[i]
        #     elif nums[i] == nums[i+1] :
        #         count+=1
        #     else :
        #         count

        # using hashing :-
        freq = {}
        for i in nums :
            if i in freq :
                freq[i]+=1
            else :
                freq[i]=1

        for k,v in freq.items() :
            if v > (len(nums)//2) :
                return k

    

        