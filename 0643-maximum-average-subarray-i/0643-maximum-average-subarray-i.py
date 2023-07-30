class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = float('-inf')
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            if i >= k - 1:
                m = max(m, s)
                s -= nums[i - k + 1]
        return m / k
