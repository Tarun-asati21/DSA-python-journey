# recursive code - TLE 

# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         final_sum = sum(nums)
#         if final_sum % 2 != 0:
#             return False

#         def backtrack(idx, total):
#             if total*2 == final_sum :
#                 return True
#             elif total > final_sum // 2 :
#                 return False
#             if idx >= len(nums) :
#                 return False
            
#             sumi = total + nums[idx]
#             pick = backtrack(idx+1, sumi)
#             if pick == True : return True

#             sumi = total
#             not_pick = backtrack(idx+1, sumi)
#             return not_pick
        
#         return backtrack(0,0)


# dp code 

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        final_sum = sum(nums)
        if final_sum % 2 != 0:
            return False
            
        target = final_sum // 2

        @lru_cache(None)
        def backtrack(idx, total):
            if total == target:
                return True
            if total > target or idx >= len(nums):
                return False
            
            # Choice 1: Include nums[idx] | Choice 2: Skip nums[idx]
            return backtrack(idx + 1, total + nums[idx]) or backtrack(idx + 1, total)

        return backtrack(0, 0)
        