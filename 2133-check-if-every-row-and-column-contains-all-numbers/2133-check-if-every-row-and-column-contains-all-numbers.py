class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r=set()
        c=set()
        l=len(matrix)
        for i in range(l):
            for j in range(l):
                v=matrix[i][j]
                k=matrix[j][i]
                if not 0<v<l+1 or not 0<k<l+1 or v in r or k in c: 
                    return False
                else :
                    r.add(v)
                    c.add(k)            
            r.clear()
            c.clear()
            
        return True