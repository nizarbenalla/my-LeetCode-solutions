class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in d.items():
            freq[count].append(num)

        l = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                l.append(j)
                if len(l) >= k:
                    return l
