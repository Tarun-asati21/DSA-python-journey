class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        vowels_map=defaultdict(int)
        consonants_map=defaultdict(int)
        vowels=set('aeiou')

        for chr in s :
            if chr in vowels :
                if chr in vowels_map :
                    vowels_map[chr]+=1
                else :
                    vowels_map[chr]=1
            else :
                if chr in consonants_map:
                    consonants_map[chr]+=1
                else :
                    consonants_map[chr]=1
        
        if len(vowels_map)==0 :
            freq_v = 0
        else :
            freq_v = max(vowels_map.values())
        
        if len(consonants_map) == 0:
            freq_c =0
        else:
            freq_c = max(consonants_map.values())     

        return freq_v + freq_c