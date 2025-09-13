class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # my approach -> counting frequency and comparing -> fails in some test cases
        # from collections import defaultdict
        # hashmap_s= defaultdict(int)
        # hashmap_t = defaultdict(int)

        # for chr in s :
        #     if chr in hashmap_s :
        #         hashmap_s[chr]+=1
        #     else:
        #         hashmap_s[chr]=1
        # for chr in t :
        #     if chr in hashmap_t :
        #         hashmap_t[chr]+=1
        #     else:
        #         hashmap_t[chr]=1
        
        # if sorted(hashmap_s.values()) == sorted(hashmap_t.values()):
        #     return True
        # else:
        #     return False

        # right approach -> 
        s_t = set(zip(s,t))
        if len(s_t)==len(set(s))==len(set(t)):
            return True
        else :
            return False