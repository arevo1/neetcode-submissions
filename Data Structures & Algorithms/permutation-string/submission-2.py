class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        f1, f2 = {}, {}
        for c in s1:
            f1[c] = f1.get(c, 0) + 1
        l = 0
        for r in range(len(s2)):
            f2[s2[r]] = f2.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                f2[s2[l]] -= 1
                if f2[s2[l]] == 0:
                    del f2[s2[l]]
                l += 1
            if f1 == f2:
                return True
        return False