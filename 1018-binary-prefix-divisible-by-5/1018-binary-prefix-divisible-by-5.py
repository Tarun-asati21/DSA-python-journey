class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = []
        num = ""
        for i in range(0, len(nums)):
            num = num + str(nums[i])
            temp = int(num, 2) 
            if temp % 5 == 0 :
                arr.append(True)
            else :
                arr.append(False)
        return arr