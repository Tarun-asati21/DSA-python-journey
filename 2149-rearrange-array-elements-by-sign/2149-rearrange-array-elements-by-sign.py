class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg =[]
        for ch in nums :
            if ch > 0 :
                pos.append(ch)
            else :
                neg.append(ch)
        
        arr =[]
        for i in range(len(pos)):
            arr.append(pos[i])
            arr.append(neg[i])
        return arr