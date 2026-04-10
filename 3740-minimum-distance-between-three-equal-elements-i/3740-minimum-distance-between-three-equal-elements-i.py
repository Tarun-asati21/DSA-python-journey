class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3 :
            return -1
        mini = float("inf")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] :
                    for k in range(j+1, len(nums)):
                        if nums[j] == nums[k] :
                            dist = abs(i-j)+abs(j-k)+abs(k-i)
                            mini = min(dist, mini)
        if mini == float("inf") :
            return -1
        return mini