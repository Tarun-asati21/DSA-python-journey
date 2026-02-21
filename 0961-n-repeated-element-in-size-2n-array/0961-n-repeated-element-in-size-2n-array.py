class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        temp = sorted(nums)
        count = 1
        for i in range(0,len(temp)-1) :
            
            if temp[i] == temp[i+1] :
                count += 1
                if count == int(n) :
                    return temp[i]

            else :
                count = 1
            
            