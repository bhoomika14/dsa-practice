"""
calculate the total number of moves required to transfer all n disks from the starting rod to the target rod
"""
def towerOfHanoi(n, A, B, C):
    global cnt
    if n>0:
        towerOfHanoi(n-1, A, B, C)
        print(f"Move {n} from {B} to {C}")
        cnt+=1
        towerOfHanoi(n-1, A, C, B)
    return cnt

cnt = 0
print(towerOfHanoi(3, 1, 2, 3))
