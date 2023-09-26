class Solution:
    def maxArea(self, height: List[int]) -> int:

        # 왼쪽과 오른쪽 커서
        left = 0
        right = len(height) - 1

        # 최대 넓이
        max_area = 0

        # 왼쪽과 오른쪽 커서가 교차할 때까지 반복
        while left < right:
            # 왼쪽과 오른쪽 커서 사이의 높이가 더 작은 값을 순회
            lower_height = min(height[left], height[right])

            # 넓이를 계산
            area = lower_height * (right - left)

            # 최대 넓이를 갱신
            max_area = max(max_area, area)

            # 더 작은 높이의 커서를 이동
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
