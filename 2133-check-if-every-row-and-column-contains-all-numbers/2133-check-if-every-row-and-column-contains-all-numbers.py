class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r=set()
        c=set()
        l=len(matrix)
        for i in range(l):
            for j in range(l):
                if not 0<matrix[i][j]<l+1 or not 0<matrix[j][i]<l+1 or matrix[i][j] in r or matrix[j][i] in c: 
                    return False
                else :
                    r.add(matrix[i][j])
                    c.add(matrix[j][i])            
            r.clear()
            c.clear()
            
        return True