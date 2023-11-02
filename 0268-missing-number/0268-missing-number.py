class Solution:
    def missingNumber(self ,nums: List[int]) -> int:
        list.sort(nums)
        if nums[0]!=0: return 0
        for i in range(1,len(nums)):
            if nums[i]-1!=nums[i-1]: 
                return nums[i]-1
        return nums[len(nums)-1]+1
