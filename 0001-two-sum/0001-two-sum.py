class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)): # 2
            i_num = nums[i]
            for j in range(1, len(nums)): # 7
                j_num = nums[j]
                if i == j:
                    break
                if i_num + j_num == target:
                    output.append(i)
                    output.append(j)
                    return output

        