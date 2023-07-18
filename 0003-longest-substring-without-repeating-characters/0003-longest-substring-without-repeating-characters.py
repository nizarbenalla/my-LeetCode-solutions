class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_window = 0
        if len(s) < 2:
            return len(s)
        for right in range(len(s)):
            if s[right] in s[left:right]:
                left += s[left:right].index(s[right]) + 1
            max_window = max(max_window, right - left + 1)
        return max_window
