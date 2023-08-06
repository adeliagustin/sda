
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j][0] > data[j+1][0]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        if not swapped:
            break

data = [
    ["Fahmi", "Jakarta"],
    ["Romi", "Solo"],
    ["Andri", "Jakarta"],
    ["Fadillah", "Banyuwangi"],
    ["Ruli", "Bandung"],
    ["Rudi", "Bali"],
    ["Dendi", "Purwokerto"],
    ["Zaki", "Madiun"]
]

bubble_sort(data)

print("Hasil Bubble Sort:")
for item in data:
    print(item[0], item[1])
