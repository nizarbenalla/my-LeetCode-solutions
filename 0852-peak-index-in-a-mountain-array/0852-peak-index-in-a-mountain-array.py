class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxi = - inf

        for i in range(len(arr)):
            oldmax = maxi
            if maxi < arr[i] : maxi = arr[i]
            if oldmax == maxi : return i-1