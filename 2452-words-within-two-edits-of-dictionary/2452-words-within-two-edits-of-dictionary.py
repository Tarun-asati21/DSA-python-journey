class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def possible(s1, s2) :
            edit = 0
            for i in range(len(s1)) :
                if s1[i] != s2[i] :
                    edit +=1
                if edit==3 :
                    return False 
            return True 

        ans =[]
        for query in queries :
            for check in dictionary :
                temp = possible(query, check)
                if temp :
                    ans.append(query)
                    break 
        return ans 