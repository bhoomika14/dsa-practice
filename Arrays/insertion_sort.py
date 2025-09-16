def insertion_sort(nums):
    for i in range(1, len(nums)):
        val = nums[i]
        j = i-1
        while j>=0 and val<nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = val

    return nums

nums = [5, 4, 1, 2, 7, 9]
print(insertion_sort(nums))

    