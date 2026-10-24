class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for s in strs:
            code = [str(0)] * 26
            print(s)
            for ch in s:
                ind = ord(ch) - 97
                code[ind] = str(int(code[ind]) + 1)
            
            merged = " ".join(code) #unique hash for each word

            if merged not in dict.keys():
                dict[merged] = [s]
            else:
                dict[merged].append(s)
                
        anagrams = []
        for list in dict.values():
            anagrams.append(list)
        return anagrams
        
        
        
        
        
        