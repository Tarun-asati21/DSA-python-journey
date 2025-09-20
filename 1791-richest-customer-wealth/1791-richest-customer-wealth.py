class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi=0
        for ch in accounts:
            wealth=sum(ch)
            maxi=max(maxi,wealth)
        return maxi