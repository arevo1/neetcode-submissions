class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join([ch for ch in s if ch.isalnum()])
        return word.lower() == word.lower()[::-1]