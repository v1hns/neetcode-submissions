class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s1 = set(s)
        n = 0
        for c in s1:
            l = 0
            count = 0
            r = 1
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                n = max(n, r-l+1)
        return n 
                
