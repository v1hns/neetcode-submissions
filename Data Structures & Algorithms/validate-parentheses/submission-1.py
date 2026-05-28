class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opn = set(["[", "(", "{"])
        cls = set(["]", ")", "}"])
        d = {']':'[', '}':'{', ')':'('}

        for i in s:
            if i in opn:
                stack.append(i)

            if i in cls:
                if not stack or d[i] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0