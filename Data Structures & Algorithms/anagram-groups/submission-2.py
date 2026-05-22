class Solution:
    def sort(self, s):
        d = dict()
        for i in s: 
            if i in d: d[i] += 1
            else: d[i] = 1
        w = ""
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in d: w = w + i * d[i]
        return w
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for i in strs:
            l.append(self.sort(i))
        d = dict()
        for i in range(len(l)):
            if l[i] in d: d[l[i]].append(i)
            else: d[l[i]] = [i]
        l1 = []
        for i in d:
            l2 = []
            for j in d[i]:
                l2.append(strs[j])
            l1.append(l2)
        return l1
                


            
        
        

            
            

            