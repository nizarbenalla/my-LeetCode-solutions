class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=0
        nums = set(nums)
        for i in nums:
            n=1
            temp=i
            if i-1 in nums: continue 
            while temp+1 in nums:
                n+=1
                temp+=1
            m= max(m,n)
        return m