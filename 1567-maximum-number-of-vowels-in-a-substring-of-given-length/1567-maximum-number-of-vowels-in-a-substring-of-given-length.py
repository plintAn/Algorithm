class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        count = 0
        max_count = 0  

        for i in range(len(s)):
            if s[i] in "aeiou":
                count += 1  # 모음 문자 개수 증가
            if i >= k - 1:
                max_count = max(max_count, count)  # 최대 모음 문자 개수 갱신
                count -= 1 if s[i - k + 1] in "aeiou" else 0  
                # 이전 문자가 모음 문자인 경우 모음 문자 개수 감소

        return max_count
