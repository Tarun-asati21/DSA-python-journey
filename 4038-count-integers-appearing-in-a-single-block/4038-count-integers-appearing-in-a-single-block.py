class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        # first starting index stored in dict
        freq_start = {}
        for i in range(0, len(nums)) :
            if nums[i] in freq_start :
                continue
            else :
                freq_start[nums[i]] = i

        # last index stored in dict
        freq_end = {}
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in freq_end :
                continue
            else :
                freq_end[nums[i]] = i
        
        ans = 0
        for k_1 , v_1 in freq_start.items() :
            v_2 = freq_end.get(k_1)
            if set(nums[v_1:v_2+1]) == set([k_1]) :
                ans += 1
        
        return ans