class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap solution - O(n), O(n)
        # seen = {}
        # for i, num in enumerate(numbers):
        #     if target-num in seen :
        #         return [seen[target-num] + 1, i+1]
        #     else :
        #         seen[num] = i

        # binary search solution - (O(n) Time, O(1) Space)
        l, r = 0, len(numbers)-1
        while l<=r :
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target :
                return [l+1, r+1]
            elif cur_sum < target :
                l +=1 
            else :
                r-=1
        