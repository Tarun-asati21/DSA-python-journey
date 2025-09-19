class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        lst=[]
        for num in nums :
            if num%2==0:
                lst.append(0)
            else :
                lst.append(1)
        result= sorted(lst)
        return result
