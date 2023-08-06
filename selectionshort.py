
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j][0] < data[min_idx][0]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

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

selection_sort(data)

print("Hasil Selection Sort:")
for item in data:
    print(item[0], item[1])
