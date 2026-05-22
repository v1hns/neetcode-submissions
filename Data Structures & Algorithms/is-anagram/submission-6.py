class Solution:
    def uniquize(self, s):
        setty = dict()
        for i in s:
            if i not in setty:
                setty[i] = 1
            else:
                setty[i] += 1
        return setty

    def isAnagram(self, s: str, t: str) -> bool:
        return self.uniquize(s) == self.uniquize(t)
        