class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_str1 = list(s)
        print(check_str1)
        check_str1 =sorted(check_str1)
        check_str2 = sorted(list(t))
        print(check_str2)
        return check_str1==check_str2