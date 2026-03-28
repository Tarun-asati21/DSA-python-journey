class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0 : 
            arr=[]
            for i in range (len(code)):
                arr.append(0)
            return arr
        # extended array use 
        temp=[]
        for i in range(2):
            for ch in code :
                temp.append(ch)
        if k > 0 :
            arr=[]
            sumi=sum(temp[1:k+1])
            for i in range (len(code)):
                arr.append(sumi)
                sumi = sumi -temp[i+1] + temp[k+i+1]
            return arr
        if k < 0 :
            arr=[]
            k=abs(k)
            sumi=sum(temp[len(code)-k : len(code)])
            for i in range(len(code)):
                arr.append(sumi)
                sumi = sumi - temp[i+len(code)-k] + temp[i+len(code)]
            return arr
