class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map1, l = {}, 0
        r = len(s1) - 1
        for i in range(len(s1)):
            freq_map1[s1[i]] = freq_map1.get(s1[i], 0) + 1

        for l in range(len(s2)-len(s1) + 1):
            freq_map2 = {}
            for j in range(l, r + 1):
                freq_map2[s2[j]] = freq_map2.get(s2[j], 0) + 1
            
            if freq_map1 == freq_map2:
                return True
            r += 1
        return False

