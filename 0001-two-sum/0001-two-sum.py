class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # extreme brute force 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target :
        #             return[i,j]

        # optimise solution - hashmap
        freq = {}
        for i, num in enumerate(nums) :
            compliment = target - num
            if compliment in freq :
                return [freq[compliment],i]
            freq[num] = i
        