class Spreadsheet:

    def __init__(self, rows: int):
        self.table = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col,row=ord(cell[0])-65,int(cell[1:])-1
        self.table[row][col]=value

    def resetCell(self, cell: str) -> None:
        col,row=ord(cell[0])-65,int(cell[1:])-1
        self.table[row][col]=0

    def getValue(self, formula: str) -> int:
        X,Y=formula[1:].split('+')
        def check(s):
            if s.isdigit():
                return int(s)
            col,row=ord(s[0])-65,int(s[1:])-1
            return self.table[row][col]
        return check(X)+check(Y)

f=Spreadsheet(3)
print(f.getValue('=5+7'))
f.setCell('A1',10)
print(f.getValue('=A1+6'))
f.setCell('B2',15)
print(f.getValue('=A1+B2'))
f.resetCell('A1')
print(f.getValue('=A1+B2'))