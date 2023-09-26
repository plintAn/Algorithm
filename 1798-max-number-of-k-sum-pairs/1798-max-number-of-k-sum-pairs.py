class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # 각 숫자가 배열에 몇 번 나타나는지 저장하는 해시 테이블을 생성
        count_table = {}
        for num in nums:
            count_table[num] = count_table.get(num, 0) + 1

        # 쌍의 개수를 0으로 초기화
        num_operations = 0

        # 해시 테이블을 순회합니다.
        for num, count in count_table.items():
            # 목표 합이 현재 숫자의 두 배인 경우,
            # 현재 숫자의 모든 쌍을 제거할 수 있다
            if k == 2 * num:
                num_operations += count // 2

            # 목표 합이 현재 숫자의 두 배보다 큰 경우,
            # 현재 숫자와 목표 합의 보수를 쌍으로 하여 제거할 수 있다
            elif k > 2 * num:
                complement = k - num
                if complement in count_table:
                    num_operations += min(count, count_table[complement])

        return num_operations
