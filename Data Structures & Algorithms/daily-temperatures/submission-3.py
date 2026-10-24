class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [] #(i, t)

        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]:
                stackInd, stackTemp = s.pop() #(0, 30)
                res[stackInd] = i - stackInd
            s.append((i, t))
        
        return res