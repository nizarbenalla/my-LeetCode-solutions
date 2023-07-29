class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10 :
            return []
        ans=[]
        d=defaultdict(int)
        right = 0
        for left in range (9,len(s)):
            d[s[right:left+1]]+=1
            right+=1
        return [i for i in d if d[i]>1]
                