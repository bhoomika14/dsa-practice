# Time complexity - O(N+M), Space complexity - O(N+M)
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


# Time complexity - O(N log N + M log M), Space complexity - O(K)
def missing_numbers(arr, brr):
    a=b=0
    result = set()
    arr.sort()
    brr.sort()
    while b<len(brr):
        if arr[a]^brr[b]!=0:
            result.add(brr[b])
            b+=1
        else:
            a+=1
            b+=1
    return result

arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]

print(missing_numbers(arr, brr))

