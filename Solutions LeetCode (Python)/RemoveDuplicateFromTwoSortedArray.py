class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[left] = nums[j]
                left += 1
        return left


