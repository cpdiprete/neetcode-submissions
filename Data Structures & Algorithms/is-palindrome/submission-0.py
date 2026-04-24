class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.upper()
        print(s)
        tail = len(s) - 1
        head = 0
        while tail >= head:
            if (s[tail] != s[head]):
                return False
            tail -= 1
            head += 1
        return True
        