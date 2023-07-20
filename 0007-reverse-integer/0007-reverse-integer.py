class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        reverse =0
        while temp > 0 :
            reverse = reverse * 10 + temp%10
            temp = temp//10
        if x<0 : reverse*=-1
        return 0 if pow(2,31)-1<abs(reverse) else reverse