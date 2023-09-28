class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        `nums` 배열의 길이가 `n`이고, `k`가 주어질 때, `k`개 이하의 `0`을 뒤집어서 만들 수 있는 가장 긴 연속된 `1`의 개수를 반환

        반환값: `k`개 이하의 `0`을 뒤집어서 만들 수 있는 가장 긴 연속된 `1`의 개수
        """

        left = 0
        right = 0
        max_count = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
            right += 1

        return max_count
