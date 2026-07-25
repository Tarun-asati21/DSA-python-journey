class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_count= len(set(arr))
        temp=sorted(arr)
        freq={}
        rank=0
        for ch in temp :
            if ch in freq :
                continue
            else :
                rank+=1
                freq[ch] = rank
        
        ans=[]
        for ch in arr :
            rank = freq.get(ch)
            ans.append(rank)
        return ans