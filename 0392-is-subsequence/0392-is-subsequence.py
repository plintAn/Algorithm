class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_arr = list(s)
        t_arr = list(t)

        i = 0
        j = 0

        while i < len(s_arr) and j < len(t_arr):
            if s_arr[i] == t_arr[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s_arr)

