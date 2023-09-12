class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split())) 
        #공백을 기준으로 리스트를 나누고 순서 반대로
