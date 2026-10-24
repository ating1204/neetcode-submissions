class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for x in s:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        for y in t:
            if y not in dict:
                return False
            dict[y] -= 1
            if dict[y] == -1:
                return False
        if sum(dict.values()) != 0:
            return False
        return True

        