class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries :
            idx = query[0]
            while  idx <= query[1] :
                nums[idx] = (nums[idx]*query[3]) % (10**9 + 7)
                idx += query[2]
        
        xor = 0
        for num in nums  :
            xor^=num
        return  xor