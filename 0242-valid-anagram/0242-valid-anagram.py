class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) : return False
        d={}
        for i, j in zip(s, t):
            if i not in d:
                d[i] = 0
            if j not in d:
                d[j] = 0
            d[i] += 1
            d[j] -= 1
        for i in d:
            if d[i] != 0:
                return False
        return True