class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            if i in s: 
                s.remove(i)
            else: 
                return i