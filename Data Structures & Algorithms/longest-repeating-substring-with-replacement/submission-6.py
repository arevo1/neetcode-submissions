class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res,l,maxf,freq_map = 0,0,0,{}

        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            maxf = max(maxf, freq_map[s[r]])

            while (r - l + 1) - maxf > k:
                freq_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        