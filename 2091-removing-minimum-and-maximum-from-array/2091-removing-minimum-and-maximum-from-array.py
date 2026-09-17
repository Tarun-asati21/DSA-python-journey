class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi =max(nums)
        mini = min(nums)

        total = len(nums)
        for i,num in enumerate(nums) :
            if num == maxi :
                maxi_idx = i
            if num == mini :
                mini_idx = i
            continue
        
        full_front = max(maxi_idx,mini_idx) + 1
        full_back = total - min(maxi_idx, mini_idx)
        front_back = min(maxi_idx,mini_idx) + 1 + total - max(maxi_idx, mini_idx)
        return min(full_front, full_back, front_back)
