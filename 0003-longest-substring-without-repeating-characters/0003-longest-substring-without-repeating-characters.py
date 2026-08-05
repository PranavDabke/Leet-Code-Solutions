class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maximumLength = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            currentLength = right - left + 1
            maximumLength = max(maximumLength, currentLength)

        return maximumLength