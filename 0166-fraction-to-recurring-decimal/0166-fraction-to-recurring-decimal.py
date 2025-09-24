class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 :
            return "0"
        if numerator % denominator == 0 :
            return str(numerator//denominator)

        # handles float division
        fraction=[]
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0) :
            fraction.append("-") # inserts -ve sign
        dividend=abs(numerator)
        divisor=abs(denominator)
        fraction.append(str(dividend//divisor)) # inserts integral quotient
        remainder = dividend % divisor
        fraction.append(".") # inserts decimal point

        hashmap={}
        while remainder !=0 :
            if remainder in hashmap :
                fraction.insert(hashmap[remainder], "(") # uss index no, me jaake ghusa do
                fraction.append(")") # at last ghusa do
                break
            hashmap[remainder]=len(fraction) # value me uska fraction array ka index store kar rahe hai
            remainder *=10 # decimal pt ki vajah se 0 lene milta hai , isliye!!
            fraction.append(str(remainder//divisor)) # inserts decimal quotient
            remainder %= divisor # naya remainder
        return "".join(fraction)




        