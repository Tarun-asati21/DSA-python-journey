class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            temp = nums[i]
            # pair = nums[i]
            for j in range (i+1, len(nums)):
                temp |= nums[j]
                pair = nums[i] | nums[j]
                if (bin(temp)[2:])[-1] == "0" or (bin(pair)[2:])[-1] == "0":
                    return True
        return False