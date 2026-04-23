class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # # brute force solution : TC = O(n^2)
        # arr = []
        # n = len(nums)
        # for i in range(0, n):
        #     ans = 0
        #     for j in range(0, n) :
        #         if j==i :
        #             continue 
        #         elif nums[j] == nums[i] :
        #             ans += abs(i-j)
        #         else :
        #             continue
        #     arr.append(ans)
        # return arr

        # # better solution : still TC = O(n^2)
        # mp = defaultdict(list)
        # for i, num in enumerate(nums):
        #     mp[num].append(i)
        
        # arr=[]
        # for i, num in enumerate(nums) :
        #     indices = mp[num]
        #     if len(indices) == 1 :
        #         arr.append(0)
        #         continue
            
        #     result = 0
        #     for idx in indices :
        #         if idx != i :
        #             result+= abs(i-idx)
        #     arr.append(result)
        # return arr 

        # optimise solution : TC = O(n)
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)

        n = len(nums)
        ans = [0] * n

        for indices in mp.values():
            k = len(indices)
            if k == 1:
                continue

            # Build prefix sum array
            # prefix[i] = sum of indices from 0 to i
            prefix = [0] * k
            prefix[0] = indices[0]
            for i in range(1, k):
                prefix[i] = prefix[i-1] + indices[i]

            # Calculate result using formulas
            for i in range(k):
                idx = indices[i]

                # LEFT SIDE CONTRIBUTION
                # Formula:
                # no of element in left - sum of all left elements
                left = i * idx - (prefix[i-1] if i > 0 else 0)

                # RIGHT SIDE CONTRIBUTION
                # Formula:
                # sum of all right elements - no of element in right
                right = (prefix[k-1] - prefix[i]) - (k - i - 1) * idx

                # Total distance
                ans[idx] = left + right

        return ans
