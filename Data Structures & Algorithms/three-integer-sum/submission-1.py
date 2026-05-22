class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #dict of index sums for each thing for instant lookup there 
        d1 = dict()
        s = set()
        for i in range(len(nums)): 
            for j in range(len(nums)): 
                i1, j1 = i, j
                if i1 > j1: j1, i1 = i1, j1
                if i1 != j1 and (i1, j1) not in s: 
                    if (nums[i1]+nums[j1]) not in d1:
                        d1[nums[i1]+nums[j1]] = [(i1, j1)]
                    else: 
                        d1[nums[i1]+nums[j1]].append((i1, j1))
                    s.add((i1, j1))
        l = []
        s2 = set()
        s3 = set()
        for i in range(len(nums)):
            if (-nums[i]) in d1:
                for j in d1[-nums[i]]:
                    (a, b) = j
                    if a != i and i != b: 
                        ns = [a, i, b]
                        idx1 = ns.pop(ns.index(min(ns)))
                        idx3 = ns.pop(ns.index(max(ns)))
                        idx2 = ns[0]
                        if (idx1, idx2, idx3) not in s2:
                            s2.add((idx1, idx2, idx3))
                            ns1 = [nums[idx1], nums[idx2], nums[idx3]]
                            n1 = ns1.pop(ns1.index(min(ns1)))
                            n3 = ns1.pop(ns1.index(max(ns1)))
                            n2 = ns1[0]
                            if (n1, n2, n3) not in s3:
                                s3.add((n1, n2, n3))
                                l.append([nums[idx1], nums[idx2], nums[idx3]])
        return l

                    


            
        
