class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        make a dictionary d1 of s1, and then initialize a sliding window of length n. if s2 < s1 in length, return false.

        otherwise, start by adding the frst n letters in s2 to a dict d2. iterate through r? bascially the string. log the character & count in the dict. if d1 = d2 at any point reutnr true

        as you move the sliding window, youd want to remve the left most letter from the dict, add the rightmost. add edge cases when left count = 1, right letter isnt in dict (.get(s2[r], 0)) i believe

        '''
        if len(s1) > len(s2):
            return False

        d1 = {}
        for ch in s1:
            d1[ch] = d1.get(ch, 0) + 1
        
        n = len(s1)
        d2 = {}
        for i in range(n):
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        if d1 == d2:
            return True
        print(d1)

        for r in range(n, len(s2)): #check if next window is g
            newCh = s2[r]
            d2[newCh] = 1 + d2.get(newCh, 0)
            leftCh = s2[r-n]
            d2[leftCh] = d2[leftCh] - 1

            if d2[leftCh] == 0:
                del d2[leftCh]
            if d1 == d2:
                return True
            
        return False

            

        

