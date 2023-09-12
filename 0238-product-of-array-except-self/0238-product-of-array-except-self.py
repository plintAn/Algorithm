class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) #nums 길이
        
        # 결과 배열 초기화
        result = [1] * n
        
        # 왼쪽의 곱 계산
        left_result = 1
        for i in range(1, n):
            left_result *= nums[i - 1]
            result[i] *= left_result
        
        # 오른쪽의 곱 계산
        right_result = 1
        for i in range(n - 2, -1, -1):
            right_result *= nums[i + 1]
            result[i] *= right_result
        
        return result
