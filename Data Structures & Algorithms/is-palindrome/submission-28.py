class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1

        if a == b:
            return True

        while a < b:

            if s[a].isalnum() and (s[b].isdigit() or s[b].isalpha()):
                if s[a].lower() != s[b].lower():
                    return False
                a += 1
                b -= 1
            else:
                if not s[a].isalpha() and not s[a].isdigit():
                    a += 1
                if not s[b].isalpha() and not s[b].isdigit():
                    b -= 1
        return True

