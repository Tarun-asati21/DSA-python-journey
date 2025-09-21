class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force -> linear search
        # lst=[]
        # for i in range(0,len(nums)):
        #     count=0
        #     for j in range (0, len(nums)):
        #         if nums[j]<nums[i]:
        #             count+=1
        #     lst.append(count)
        # return lst

        # better solution -> binary search-lowerbound
        sort_nums=sorted(nums)
        lst=[]
        for num in nums :
            mini=len(nums)
            l=0
            r=len(nums)-1
            while l<=r :
                m=(l+r)//2
                if sort_nums[m]>=num :
                    mini=min(mini,m)
                    r=m-1
                else :
                    l=m+1
            lst.append(mini)
        return lst
