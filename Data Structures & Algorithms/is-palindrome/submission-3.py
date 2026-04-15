class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        reverse = res[::-1]
        return res == reverse