class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #should be in pairs [ind, temp]

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append([ind, temp])
        return res
