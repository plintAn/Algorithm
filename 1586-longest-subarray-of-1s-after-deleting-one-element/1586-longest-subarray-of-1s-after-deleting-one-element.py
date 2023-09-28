class Solution:
    def longestSubarray(self, nums: List[int]) -> int:


        # 가장 긴 부분 배열의 길이, 0의 개수, 현재 부분 배열의 시작 인덱스를 초기화
        ans = zeros = left = 0

        # 배열을 순회하며 다음을 수행
        for i in range(len(nums)):
            # 현재 인덱스의 값이 0이면 0의 개수를 1 증가
            zeros += (nums[i] == 0)

            # 0의 개수가 2 이상이면, 현재 부분 배열의 시작 인덱스를 0의 개수만큼 왼쪽으로 이동
            while zeros > 1:
                zeros -= (nums[left] == 0)
                left += 1

            # 현재 부분 배열의 길이를 업데이트
            ans = max(ans, i - left)

        # 결과를 반환
        return ans
