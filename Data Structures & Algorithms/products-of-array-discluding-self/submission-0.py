class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        nz = 0
        for i in range(len(nums)): 
            if nums[i] != 0:
                n *= nums[i]
            else: 
                nz += 1
        if nz > 1: 
            return [0] * len(nums)
        elif nz == 0: 
            l = []
            for i in nums:
                if i != 0:
                    l.append(n//i)
                else:
                    l.append(n)
        else: 
            l = []
            for i in nums:
                if i != 0:
                    l.append(0)
                else:
                    l.append(n)
        return l

        

            