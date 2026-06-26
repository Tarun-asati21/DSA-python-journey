class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1 :
            return False
        lst = sorted(nums)
        maxi = lst[-1]
        if lst[-1] != lst[-2] :
            return False 
        elif lst[0] != 1 :
            return False
        elif len(lst) != maxi + 1 : 
            return False
        elif len(lst) > 3 :
            for i in range(len(lst)-3, 0, -1) :
                if lst[i] != lst[i-1] + 1 :
                    return False
        elif len(lst) == 3 :
            if lst[1] == 1 :
                return False
        return True

        