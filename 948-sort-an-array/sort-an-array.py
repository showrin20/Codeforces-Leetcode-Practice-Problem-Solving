class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(sorted_left, sorted_right):
            result = []
            i, j = 0, 0

            while i < len(sorted_left) and j < len(sorted_right):
                if sorted_left[i] < sorted_right[j]:
                    result.append(sorted_left[i])
                    i += 1
                else:
                    result.append(sorted_right[j])
                    j += 1
            result.extend(sorted_left[i:])
            result.extend(sorted_right[j:])
            return result

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            sorted_left = merge_sort(left)
            sorted_right = merge_sort(right)
            return merge(sorted_left, sorted_right)

        return merge_sort(nums)
