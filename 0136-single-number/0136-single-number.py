class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force solution
        # freq={}
        # for num in nums :
        #     if num in freq :
        #         freq[num]+=1
        #     else :
        #         freq[num]=1

        # for key, value in freq.items():
        #     if value==1 :
        #         return key

        # better solution
        n=len(nums)
        hash_list ={}
        for i in range(0,n):
            hash_list[nums[i]]=hash_list.get(nums[i],0)+1
        
        for key, value in hash_list.items():
            if value==1 :
                return key