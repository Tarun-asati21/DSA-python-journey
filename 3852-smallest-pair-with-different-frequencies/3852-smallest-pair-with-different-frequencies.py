class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = {}
        for ch in nums :
            if ch in freq :
                freq[ch]+=1
            else :
                freq[ch]=1

        unique = sorted(freq.keys())
        
        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                if freq[unique[i]] != freq[unique[j]]:
                    return [unique[i], unique[j]]
  
        return [-1, -1]