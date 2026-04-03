class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def count(x : str) -> int:
            count_1 = 0
            for ch in x :
                if ch == "1" :
                    count_1 +=1 
            return count_1

        sumi = 0
        for i in range (0, len(nums)) :
            temp = bin(i)[2:]
            if count(temp) == k :
                sumi += nums[i]

        return sumi