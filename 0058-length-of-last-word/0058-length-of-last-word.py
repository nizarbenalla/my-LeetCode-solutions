class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        answer =0
        wordIndex=len(s)-1
        
        while s[wordIndex]==' ':
                wordIndex-=1
        
        while s[wordIndex]!=' ' and wordIndex>=0 :
            answer+=1
            wordIndex-=1
        return answer
