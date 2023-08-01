class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        
        left=0
        right=len(s)-1
        
        while right>=left:
            
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left] != s[right]:
                print(s)
                return False
            right-=1
            left+=1
        return True
        