class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abccabc

        if empty return 0

        l = 0
        r = 0

        [l, r]

        ....zz
        ..z..z....
        {..., z,..}
        if s[r] in set:
            l += 1
            empty set
        l....r
        '''

        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        max = 1
        l = 0
        r = 1 #[2, 2, 3, 4, 4], len = 5
        
        letters = set(s[l])

        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
                if len(letters) > max:
                    max = len(letters)
            else:
                if r == l:
                    r += 1
                else:
                    letters.remove(s[l])
                    l += 1
                    print(letters)
        return max





            



