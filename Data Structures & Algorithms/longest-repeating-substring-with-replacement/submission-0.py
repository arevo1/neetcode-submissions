class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        for i in range(len(s)):
            freq_map,maxf = {},0
            for j in range(i, len(s)):
                freq_map[s[j]] = freq_map.get(s[j],0) + 1 
                maxf = max(maxf, freq_map[s[j]])
                rep = (j - i + 1) - maxf
                if rep <= k:
                    res = max(res, rep)
        return res
                


        
