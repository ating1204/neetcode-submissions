class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for s in strs:
            l = [0] * 26
            for ch in s:
                x = ord(ch) - ord('a')
                l[x] += 1
            key = tuple(l)

            if key not in dict.keys():
                dict[key] = []
            dict[key].append(s)
        return list(dict.values())