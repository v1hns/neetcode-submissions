import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        cl = []
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d: 
                print(i, nums[i], d[nums[i]])
                print(cl)
                cl[d[nums[i]]] += 1
            else: 
                l.append(nums[i])
                cl.append(1)
                d[nums[i]] = len(cl) - 1
                print('here ' + str(cl) + ' and ' + str(d[nums[i]]) + ' and ' + str(i))
        nl = []
        while k > 0:
            nl.append(l.pop(np.argmax(cl)))
            cl.pop(np.argmax(cl))
            k -= 1
        return nl
        
        

            

            

       
        
        