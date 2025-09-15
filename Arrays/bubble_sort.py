# Time complexity - O(N^2), Space complexity - O(1)
def bubble_sort(nums):
    swapped = False
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped!=True:
            return -1

    return nums

nums = [5, 6, 2, 4, 3]
print(bubble_sort(nums))