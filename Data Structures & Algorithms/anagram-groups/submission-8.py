class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        tuple = (0) * 26
        make hm of key = tuple, value = list of anngrams? return list(values)?

        '''
        hm = {}

        for s in strs:
            v = [0] * 26
            for ch in s:
                v[ord(ch) - ord('a')] += 1
            key = tuple(v)
            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)
            
        return list(hm.values())