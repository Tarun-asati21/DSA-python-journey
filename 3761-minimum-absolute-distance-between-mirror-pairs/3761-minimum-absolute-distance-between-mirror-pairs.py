class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # # brute force :- 
        # if len(nums) == 1:
        #     return -1

        # def reverse(x):
        #     temp = str(x)
        #     ans = ""
        #     for ch in temp  :
        #         ans = ch + ans
        #     ans = int(ans)
        #     return ans
        
        # temp_arr = []
        # for num in nums :
        #     temp_arr.append(reverse(num))
        
        # mini = float("inf")
        # for i in range(0, len(temp_arr)-1) :
        #     for j in range(i+1, len(nums)) :
        #         if nums[j] == temp_arr[i] :
        #             diff = abs(i-j)
        #             mini = min(mini,diff)
        
        # if mini == float("inf") :
        #     return -1
        # return mini

        # optimize solution :- 
        def reverse(x):
            return int(str(x)[::-1])
        
        index_map = {}  
        mini = float("inf")
        for i, num in enumerate(nums):
            
            rev = reverse(num)

            if num in index_map:
                mini = min(mini, i - index_map[num])

            index_map[rev] = i
        
        return -1 if mini == float("inf") else mini