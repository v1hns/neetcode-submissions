class Solution:
    def arePermutations(self, a, b):
        if len(a) != len(b): return False
        d1, d2 = dict(), dict()
        for i in range(len(a)):
            if a[i] in d1: d1[a[i]] += 1 
            else: d1[a[i]] = 1
            if b[i] in d2: d2[b[i]] += 1 
            else: d2[b[i]] = 1
        return d1 == d2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        for i in range(len(s2)-j+1):
            if self.arePermutations(s2[i:i+j],s1): return True
        return False
