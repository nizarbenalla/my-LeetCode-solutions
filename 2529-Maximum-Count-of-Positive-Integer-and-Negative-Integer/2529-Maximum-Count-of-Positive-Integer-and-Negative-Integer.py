class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        zero=0
        for i in nums:
            if i<0:
                neg+=1
            if i==0:
                zero+=1
            if i>0:
                return max(neg, len(nums)-zero-neg)
        return neg
        
