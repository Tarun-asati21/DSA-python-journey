class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={}
        lst=[]
        for num in nums :
            if num  not in hashmap :
                hashmap[num]=1
            else :
                lst.append(num)
        return lst
            