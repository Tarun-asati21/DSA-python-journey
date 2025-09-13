class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        from collections import defaultdict
        hashmap = defaultdict(int)

        for chr in s :
            if chr in hashmap :
                hashmap[chr]+=1
            else :
                hashmap[chr]=1
        
        freq=sorted(hashmap.items(), key=lambda x : x[1],reverse=True)
        sorted_s=""
        for key,value in freq :
            sorted_s+=key*value

        return sorted_s
            