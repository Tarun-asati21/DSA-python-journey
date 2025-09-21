class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        lst=[]
        for candy in candies :
            if (candy + extraCandies) >= max_candies :
                lst.append(True)
            else :
                lst.append(False)
        return lst