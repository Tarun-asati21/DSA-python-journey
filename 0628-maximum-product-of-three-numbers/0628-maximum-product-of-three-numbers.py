class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            prod=1
            for num in nums :
                prod*=num
            return prod
        
        pos = []
        neg_ac = []
        for num in nums :
            if num < 0 :
                neg_ac.append(num)
            else :
                pos.append(num)

        pos.sort()
        neg_ac.sort()
        neg=[]
        for num in neg_ac :
            neg.append(abs(num))
        neg.sort()

        if len(pos) == 0 :
            return neg_ac[-1]*neg_ac[-2]*neg_ac[-3]
        if len(neg) == 0 :
            return pos[-1]*pos[-2]*pos[-3]
        # possible cases 
        if len(pos) >= 3 :
            c1 = pos[-1]*pos[-2]*pos[-3]
            if len(neg) >= 2 :
                c2 = pos[-1]*neg[-1]*neg[-2]
                c1 = max(c1,c2)
            return c1
        if len(pos) <= 2 :
            if len(neg) >= 2 :
                c3 = pos[-1]*neg[-1]*neg[-2]
            else :
                c3 = pos[-1]*pos[-2]*neg_ac[-1]
            return c3