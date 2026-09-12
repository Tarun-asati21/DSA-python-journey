# class Solution:
#     def countSpecialIntegers(self, nums: list[int]) -> int:
#         freq = {}
#         for i,num in enumerate(nums):
#             if num in freq :
#                 freq[num] = freq.get(num) + [i]
#             else :
#                 freq[num] = [i]
        
#         ans = 0
#         for value in freq.values() :
#             if len(value) < 3 :
#                 continue
#             diff = value[1]-value[0]
#             flag=True
#             for i in range(2,len(value)) :
#                 if value[i] - value[i-1] != diff :
#                     flag=False
#                     break
#             if flag==True :
#                 ans +=1
                
#         return ans
        
from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums):
        pos = defaultdict(list)

        # Store all positions for each number
        for i, x in enumerate(nums):
            pos[x].append(i)

        res = 0

        # Check each distinct number
        for positions in pos.values():

            # At least three occurrences are required
            if len(positions) >= 3:

                gap = positions[1] - positions[0]
                flag = True

                # Check whether all consecutive gaps are equal
                for i in range(2, len(positions)):
                    if positions[i] - positions[i - 1] != gap:
                        flag = False
                        break

                if flag:
                    res += 1

        return res