class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #양의 무한대 실수
        small = float('inf')
        mid = float('inf')
        #nums 리스트
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True

        return False





