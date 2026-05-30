class Solution:
    def howManyHours(self, piles, n):
        if n == 0: return 0
        sm = 0
        for i in range(len(piles)):
            sm += piles[i]//n
            if piles[i] % n != 0: sm += 1
        return sm
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb = 1
        ub = max(piles)
        while lb < ub: 
            k = (lb + ub)//2
            if self.howManyHours(piles, k) > h:
                lb = k + 1
            else:
                ub = k
        return lb
        


