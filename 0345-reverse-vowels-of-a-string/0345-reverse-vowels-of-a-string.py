class Solution:
    def reverseVowels(self, s: str) -> str:
        vol = 'AEIOUaeiou'
        s_list = [char for char in s if char in vol] 
        #문자열 s에서 vol를 포함하는 문자 추출하여 리스트
        
        return ''.join([char if #문자 결합
        char not in vol #문자가 vol에 포함하지 않은 문자일 경우 리스트 그대로 추가
        else s_list.pop() #문자가 vol에 포함되면 마지막 문자 제거 후 반환(즉, 역순)
        for char in s]) #문자열 s에 대하여 각 문자를 char로 반복
