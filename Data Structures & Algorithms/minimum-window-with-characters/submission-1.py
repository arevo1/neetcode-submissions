class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)<len(s):
            return ""
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)

        res = [-1,1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
            l, r = res

        return s[l:r+1] if res_len != float(inf) else ""