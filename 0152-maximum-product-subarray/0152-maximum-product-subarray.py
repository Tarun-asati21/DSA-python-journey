class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # brute force solution
        # lst=[]
        # size= len(nums)
        # for i in range(0,size):
        #     product = 1
        #     for j in range (i,size):
        #         product = product* nums[j]
        #         lst.append(product)
        # return max(lst)

        # optimal solution 1 -> pefix & suffix product 
        maxi=-float("inf")
        pre=1
        suff=1
        n=len(nums)
        for i in range(0,n):
            pre *= nums[i]
            suff *= nums[n-i-1]
            maxi=max(maxi,pre,suff)
            if pre== 0 :
                pre = 1
            if suff == 0:
                suff=1
        return maxi

                    