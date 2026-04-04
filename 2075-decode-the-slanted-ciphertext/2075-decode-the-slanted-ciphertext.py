class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1 :
            return encodedText

        # lst=encodedText.split()
        # columns = rows + len(lst[-1]) - 1 # this was wrong
        # since : total characters = row * columns, therefore : 
        columns = len(encodedText)//rows # this is right

        matrix =[[" " for _ in range (columns)] for _ in range (rows) ]
        idx = 0
        for i  in range(rows) :
            for j in range(columns):
                matrix[i][j] = encodedText[idx]
                idx+=1
        
        ans = ""
        for i in range(columns):
            r = 0
            c = i
            while r < rows and c < columns :
                ans+=matrix[r][c]
                r+=1
                c+=1
        return ans.rstrip()


