class Solution:
    #use ord(ch) to generalize

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            word = s[j+1: j + n + 1]
            res.append(word)
            i = j + n + 1
        return res
        
