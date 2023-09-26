class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0  # s의 인덱스
        j = 0  # t의 인덱스

        while i < len(s) and j < len(t):
            # s의 i 번째 문자와 t의 j 번째 문자가 같으면
            if s[i] == t[j]:
                # s의 인덱스와 t의 인덱스를 모두 1 증가시킵니다.
                i += 1
                j += 1
            else:
                # s의 i 번째 문자와 t의 j 번째 문자가 다르면
                # t의 인덱스를 1 증가시킵니다.
                j += 1

        # s의 인덱스가 s의 길이와 같으면 s는 t의 하위 시퀀스입니다.
        return i == len(s)
