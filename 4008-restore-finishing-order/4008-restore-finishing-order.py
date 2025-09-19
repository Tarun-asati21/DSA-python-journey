class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        lst=[]
        for a in order :
            for b in friends :
                if a==b :
                    lst.append(a)

        return lst