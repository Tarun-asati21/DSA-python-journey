class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        sorted_freq = dict(sorted(freq.items(), key = lambda items : (-items[1], items[0])))

        lst = []
        for key in sorted_freq.keys() :
            if len(lst) < k :
                lst.append(key)
        return lst