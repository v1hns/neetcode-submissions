class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + i + 'る'
        return s 
    def decode(self, s: str) -> List[str]:
        l = []
        w = ""
        for i in s:
            if i == "る": 
                l.append(w)
                w = ""
            else:
                w = w + i
        return l
