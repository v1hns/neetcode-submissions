class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l <= r:
            goal = l+(r-l)//2
            print(goal, l, r)
            if nums[goal] < target:
                l = goal + 1
            elif nums[goal] > target: 
                r = goal - 1
            else:
                return goal
        return -1