"""
Generate all possible subsets of a given set without duplicates

"""
def generate_subset(input_arr, sub_arr, input_index):
    if input_index==len(input_arr):
        print(sub_arr)
        return
    sub_arr.append(input_arr[input_index])
    generate_subset(input_arr, sub_arr, input_index+1)
    sub_arr.pop()
    generate_subset(input_arr, sub_arr, input_index+1)

generate_subset([1,2,3], [], 0)