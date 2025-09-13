class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        hashmap=defaultdict(list)

        lst=[s,t]
        for ch in lst :
            sorted_str= tuple(sorted(ch))
            hashmap[sorted_str].append(ch)
        
        if len(hashmap)==1:
            return True
        else:
            return False