class Solution:
    def compress(self, chars: List[str]) -> int:
        write = anchor = 0
        #인덱스, 값 in enumerate()
        for read, c in enumerate(chars):
            # 문자열의 끝에 도달하거나 현재 문자와 다음 문자가 다른 경우
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                
                # 현재 문자의 연속된 개수 계산
                count = read - anchor + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                        
                # anchor 갱신
                anchor = read + 1

        return write