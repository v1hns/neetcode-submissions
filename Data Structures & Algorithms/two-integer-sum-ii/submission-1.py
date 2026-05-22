class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): 
            goal = target - numbers[i]
            ln = i + 1
            rn = len(numbers) - 1
            pick = ln + (rn - ln) // 2
            while rn >= ln: 
                pick = ln + (rn - ln) // 2
                if numbers[pick] > goal: rn = pick - 1
                elif numbers[pick] < goal: ln = pick + 1
                else: return [i+1, pick+1]

