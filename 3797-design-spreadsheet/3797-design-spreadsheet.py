class Spreadsheet:

    def __init__(self, rows: int):
        # hashmap -> { cell_ref : value }
        self.cells={}
        
    def setCell(self, cell: str, value: int) -> None:
        # value store
        self.cells[cell]=value

    def resetCell(self, cell: str) -> None:
        # delete
        if cell in self.cells : 
            del self.cells[cell]
        
    def getValue(self, formula: str) -> int:
        operator = formula.index("+")
        left = formula[1:operator]
        right = formula[operator+1 :]

        if left[0].isalpha() :
            left_operand=self.cells.get(left, 0)
        else:
            left_operand = int(left)
        
        if right[0].isalpha() :
            right_operand=self.cells.get(right,0)
        else:
            right_operand = int(right)

        return left_operand + right_operand
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)