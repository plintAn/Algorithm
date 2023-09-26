import numpy as np

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # 왼쪽과 오른쪽 인덱스
        left = 0
        right = len(height) - 1

        # 최대 넓이
        max_area = 0

        # 왼쪽과 오른쪽 인덱스가 교차할 때까지 반복
        while left < right:
            # 왼쪽과 오른쪽 인덱스의 높이를 벡터로 생성
            heights = np.array([height[left], height[right]])

            # 왼쪽과 오른쪽 인덱스의 높이 중 더 작은 값을 찾습니다.
            lower_height = np.min(heights)

            # 넓이를 계산
            area = lower_height * (right - left)

            # 최대 넓이를 갱신
            max_area = max(max_area, area)

            # 더 작은 높이의 인덱스를 이동
            if heights[0] <= heights[1]:
                left += 1
            else:
                right -= 1

        return max_area
