class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # sheekne waali baaat iis sawaal ki
        sorted_dict = dict(sorted(freq.items(), key=lambda x: (x[1], -x[0])))
        
        arr = []
        for key, value in sorted_dict.items():
            for i in range(value):
                arr.append(key)
        
        return arr