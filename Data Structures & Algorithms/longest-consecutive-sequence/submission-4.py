class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        n = 1
        if nums == []: return 0
        for i in s: 
            j = i
            if (j + 1) in s:
                n1 = 0
                while (j + 1) in s:
                    j = j + 1
                    n1 += 1
                if n1 + 1 >= n: n = n1 + 1
        return n 
                

