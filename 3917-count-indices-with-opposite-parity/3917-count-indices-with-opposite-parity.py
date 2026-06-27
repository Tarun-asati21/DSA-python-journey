class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return [0]
        arr= []
        for i in range(0, len(nums)) :
            score = 0
            check = nums[i]%2 
            for j in range(i+1, len(nums)) :
                if nums[j]%2 != check :
                    score += 1
            arr.append(score)
        return arr