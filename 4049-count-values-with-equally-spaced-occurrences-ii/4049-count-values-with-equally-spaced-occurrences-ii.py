from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = defaultdict(list)
        for i,num in enumerate(nums):
            freq[num].append(i)

        ans = 0
        for value in freq.values() :
            if len(value) < 3 :
                continue
            diff = value[1]-value[0]
            flag=True
            for i in range(2,len(value)) :
                if value[i] - value[i-1] != diff :
                    flag=False
                    break
            if flag==True :
                ans +=1
                
        return ans