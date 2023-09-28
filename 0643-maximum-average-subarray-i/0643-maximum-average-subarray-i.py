class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        `k` 요소 이후의 각 요소에 대해:
        * `window_sum`에서 가장 오래된 요소를 빼고 가장 최근 요소를 더한다
        * `current_max`를 `window_sum` / `k`와 비교하여 더 큰 값을 저장

        반환값: `k` 크기의 연속 하위 배열 중에서 평균값이 가장 큰 하위 배열의 평균
        """

        first_sum = sum(nums[:k])
        current_max = first_sum / k

        for i in range(k, len(nums)):
            first_sum = first_sum - nums[i - k] + nums[i]
            current_max = max(current_max, first_sum / k)

        return current_max
