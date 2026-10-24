class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalpha():
                cleaned += ch.lower()
            if ch.isdigit():
                cleaned += ch
        
        if len(cleaned) == 0:
            return True
        print(cleaned)
        a = 0
        b = len(cleaned) - 1

        while a < b:
            if cleaned[a] != cleaned[b]:
                return False
            a += 1
            b -= 1
        return True


