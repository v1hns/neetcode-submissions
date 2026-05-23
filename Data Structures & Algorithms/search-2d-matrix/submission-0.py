class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) -1
        while l <= r:
            goal = l+(r-l)//2
            if nums[goal] < target:
                l = goal + 1
            elif nums[goal] > target: 
                r = goal - 1
            else:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = []
        for i in matrix: 
            l.extend(i)
        return self.search(l, target)