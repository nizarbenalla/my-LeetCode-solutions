class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right =0,len(nums)-1
        while left<=right:
            if nums[left + (right -left)//2]==target:
                return left + (right -left)//2
            elif target > nums[left + (right -left)//2]:
                left =( left + (right -left)//2)+1
            else :
                right = (left + (right -left)//2)-1
        return -1
