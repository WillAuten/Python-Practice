target = 44
sortedLyst = [20,44,48,55,63,66,74,88,93,99]

print("The target is", target)
print("The list is",sortedLyst)

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        print("Midpoint is currently at element", midpoint, "which has a value of",sortedLyst[midpoint])
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
            print("Right is currently at element", right, "which has a value of",sortedLyst[right])
        else:
            left = midpoint + 1
            print("Left is currently at element", left, "which has a value of",sortedLyst[left])
    return -1

binarySearch(target, sortedLyst)
