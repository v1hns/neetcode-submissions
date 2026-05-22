class Solution:
    def dictify(self, s1):
        d = dict()
        for i in s1:
            if i in d: d[i] += 1
            else: d[i] = 1
        return d
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = self.dictify(s1)
        for i in range(0, len(s2)-len(s1)+1):
            if self.dictify(s2[i:i+len(s1)]) == d1: return True
        return False

