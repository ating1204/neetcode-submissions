class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda t: (t[0], t[1]))
        # sorted by inc

        res = []
        l, u = intervals[0]
        for a,b in intervals:
            #if a within cur range and b bigger than u set u = b
            if a <= u and b <= u:
                continue
            elif a <= u and b > u:
                u = b
            else: #a > u
                res.append([l,u])
                l,u = a,b
        res.append([l,u])
        return res

