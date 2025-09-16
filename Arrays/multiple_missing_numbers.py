#Brute force - Time complexity - O(N+M)
def multiple_missing(arr, brr):
    result = []
    hashMap_arr={}
    for i in arr:
        hashMap_arr[i] = hashMap_arr.get(i, 0)+1

    hashMap_brr={}
    for i in brr:
        hashMap_brr[i] = hashMap_brr.get(i, 0)+1

    for k, v in hashMap_brr.items():
        if k in hashMap_arr:
            if v-hashMap_arr[k]!=0:
                result.append(k)
        else:
            result.append(k)

    return result

arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]

print(multiple_missing(arr, brr))

