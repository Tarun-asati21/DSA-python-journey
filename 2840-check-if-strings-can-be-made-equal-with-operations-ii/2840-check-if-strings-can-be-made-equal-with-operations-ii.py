class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        even_s1 = {}
        odd_s1= {}
        even_s2 ={}
        odd_s2={}

        for i in range(len(s1)):
            if i%2==0 :
                if s1[i] in even_s1 :
                    even_s1[s1[i]] +=1
                else :
                    even_s1[s1[i]] =1 

                if s2[i] in even_s2 :
                    even_s2[s2[i]] +=1
                else :
                    even_s2[s2[i]] = 1

            else :
                if s1[i] in odd_s1 :
                    odd_s1[s1[i]] += 1
                else :
                    odd_s1[s1[i]] =1

                if s2[i] in odd_s2 :
                    odd_s2[s2[i]] +=1
                else :
                    odd_s2[s2[i]] = 1
        
        if even_s1 == even_s2 and odd_s1 == odd_s2 :
            return True 
        return False