class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        while n > 0:
            n1 = 0
            for i in range(n, len(s) + 1):
                if len(set(s[n1:i])) == len(s[n1:i]):
                    return len(s[n1:i])
                n1 += 1
            n -= 1
        return 0 
