class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        mini = min(nums)
        maxi = max(nums) 

        lst = []
        for i in range(1, maxi+k+1) :
            if i%k == 0 :
                lst.append(i)
        
        seti = set(lst) - set(nums)
        for num in sorted(seti) :
            return num 
            break