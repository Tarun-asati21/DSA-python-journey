class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        hashmap = defaultdict(list)
        
        for i,n in enumerate(strs) :
            sorted_str = tuple(sorted(n))
            hashmap[sorted_str].append(n)
        
        return hashmap.values()