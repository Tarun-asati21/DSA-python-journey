class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        count=0
        for i in range (0,len(nums)-1) :
            sum1 = sum(nums[:i+1])
            sum2 = sum(nums[i+1:])

            if (sum1-sum2)%2 == 0 :
                count+=1
        return count