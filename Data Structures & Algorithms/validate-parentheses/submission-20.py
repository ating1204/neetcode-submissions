class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        hm = {')' : '(', ']' : '[', '}' : '{'}
        for ch in s:
            if ch in list(hm.values()):
                st.append(ch)
            else:
                if not st or st[-1] != hm[ch]:
                    return False
                st.pop()
        if st == []:
            return True
        return False