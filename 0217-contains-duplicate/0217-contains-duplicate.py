class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq =  defaultdict(int)
        for num in nums  :
            if num in freq  :
                freq[num] += 1
            else :
                freq[num] =1
        
        for value in freq.values() :
            if  value==2  :
                return True 
        return False