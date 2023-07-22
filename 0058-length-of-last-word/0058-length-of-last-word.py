class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1: 
            return 1
        answer =0
        wordIndex=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                wordIndex=i
                break
        for i in range(wordIndex,-1,-1):
            if s[i]==' ' : return answer
            answer+=1
        return answer
