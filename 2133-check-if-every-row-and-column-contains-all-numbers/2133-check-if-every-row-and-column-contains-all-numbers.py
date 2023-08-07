class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r=set()
        c=set()
        l=len(matrix)
        for i in range(l):
            for j in range(l):
                v=matrix[i][j]
                k=matrix[j][i]
                if 0<v<l+1 and 0<k<l+1 : 
                    if v in r or k in c:
                        return False
                    r.add(v)
                    c.add(k)
                else :
                    return False
            r.clear()
            c.clear()
            
        return True