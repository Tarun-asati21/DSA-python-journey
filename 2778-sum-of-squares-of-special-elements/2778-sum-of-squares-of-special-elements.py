class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        idx=1
        ans = 0
        n=len(nums)
        for num in nums:
            if n%idx == 0 :
                ans += num**2
            idx+=1
        return ans