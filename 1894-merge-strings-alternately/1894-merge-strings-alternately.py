class Solution:
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0
        
        while i < len(word1) or j < len(word2):
            #i,j가 문자열 길이보다 작은 동안 참(순회)
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1
        return ''.join(result) #''는 빈문자열 연결