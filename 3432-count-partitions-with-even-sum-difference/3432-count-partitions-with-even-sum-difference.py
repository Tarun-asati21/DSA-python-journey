class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        # brute force
        # count=0
        # for i in range (0,len(nums)-1) :
        #     sum1 = sum(nums[:i+1])
        #     sum2 = sum(nums[i+1:])

        #     if (sum1-sum2)%2 == 0 :
        #         count+=1
        # return count

        # better approach
        count=0
        sumi=sum(nums)
        sumi_left = 0
        for i in range (0,len(nums)-1):
            sumi_left += nums[i]
            sumi_right = sumi-sumi_left
            if (sumi_left-sumi_right) % 2 == 0 :
                count+=1
        return count