def binary_search(arr, target):
    result = []
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result.append(mid)
            # Pencarian untuk indeks sebelumnya
            left = mid - 1
            while left >= 0 and arr[left] == target:
                result.append(left)
                left -= 1
            # Pencarian untuk indeks setelahnya
            right = mid + 1
            while right < len(arr) and arr[right] == target:
                result.append(right)
                right += 1
            return result
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Data array
arr = [19, 40, 10, 90, 2, 50, 60, 50, 1]

# Test case
test_cases = [1, 50, 100]

for target in test_cases:
    indices = binary_search(arr, target)
    if indices:
        print(f"Angka {target} ada di indeks ke {', '.join(map(str, indices))}.")
    else:
        print(f"Angka {target} tidak ada dalam array.")

