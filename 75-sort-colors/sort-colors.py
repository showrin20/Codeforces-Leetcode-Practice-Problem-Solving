class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1

        def partition(arr, low, high):
            l = low + 1
            h = high
            pivot = arr[low]  

            while True:
                while l <= h and arr[l] <= pivot:
                    l += 1
                while l <= h and arr[h] >= pivot:
                    h -= 1

                if l <= h:
                    arr[l], arr[h] = arr[h], arr[l]  
                else:
                    break

            arr[low], arr[h] = arr[h], arr[low]  
            return h

        def quick_sort(arr, low, high):
            if low < high:  
                p_index = partition(arr, low, high)
                quick_sort(arr, low, p_index - 1)
                quick_sort(arr, p_index + 1, high)

        quick_sort(nums, low, high)
     

        