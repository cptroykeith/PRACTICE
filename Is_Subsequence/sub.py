class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_ptr = 0
        s_ptr = 0

        while t_ptr < len(t) and s_ptr < len(s):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

        return len(s) == s_ptr