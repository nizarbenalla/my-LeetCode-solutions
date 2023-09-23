class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n,m=1,0
        nums = set(nums)
        for i in nums:
            temp=i
            if i-1 in nums: continue 
            while temp+1 in nums:
                n+=1
                temp+=1
            m= max(m,n)
            n=1
        return m