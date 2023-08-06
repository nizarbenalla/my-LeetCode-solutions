class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        s= set()
        s2=set()
        sq= defaultdict(set)        
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                k=board[j][i]       
                if v!=".":
                    if v in s or v in sq[(i//3,j//3)] : return False
                    s.add(v)
                    sq[(i//3,j//3)].add(v)
                if k!=".":
                    if k in s2: return False
                    s2.add(k)  
            s.clear()
            s2.clear()
        s.clear()
        s2.clear()               
        return True