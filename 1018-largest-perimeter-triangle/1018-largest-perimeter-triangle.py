class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # # brute force - O(n^3) --> TLE
        # lst =[0]
        # n = len(nums)
        # for i in range (0,n) :
        #     a=nums[i]
        #     for j in range(i+1, n):
        #         b=nums[j]
        #         for k in range (j+1,n):
        #             c=nums[k]
        #             if a+b > c and b+c > a and c+a> b : # triangle inequality theorem 
        #                 perimeter = a+b+c
        #                 lst.append(perimeter)
        # return max(lst)

        # optimal solution - O(nlogn)  --> greedy approach used!!
        nums.sort()
        n=len(nums)
        for i in range (n-1, 1,-1):
            if nums[i-1]+nums[i-2] > nums[i] :
                return nums[i]+nums[i-1]+nums[i-2]
        return 0