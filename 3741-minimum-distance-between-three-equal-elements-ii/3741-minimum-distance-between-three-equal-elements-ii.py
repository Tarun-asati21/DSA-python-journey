class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        for i, num in enumerate(nums):
            freq[num].append(i)
        
        mini = float("inf")
        for val in freq.values() :
            m = len(val)
            if m >= 3 :
                for i in range(m-2) :
                    a = val[i]
                    b= val[i+1]
                    c=val[i+2]

                    diff = 2*(c-a)
                    mini = min(mini, diff)
        return -1 if mini==float("inf") else mini
