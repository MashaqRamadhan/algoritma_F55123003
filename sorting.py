# MERGE_SORT(arr, left, right)
# 1. If left < right:
# 2.    mid = (left + right) // 2
# 3.    MERGE_SORT(arr, left, mid)
# 4.    MERGE_SORT(arr, mid + 1, right)
# 5.    MERGE(arr, left, mid, right)

# MERGE(arr, left, mid, right)
# 1. Create temporary arrays L = arr[left..mid] and R = arr[mid+1..right]
# 2. i = 0, j = 0, k = left
# 3. While i < length(L) and j < length(R):
# 4.    If L[i] <= R[j]:
# 5.        arr[k] = L[i]
# 6.        i = i + 1
# 7.    Else:
# 8.        arr[k] = R[j]
# 9.        j = j + 1
# 10.   k = k + 1
# 11. Copy any remaining elements of L and R into arr


# ### **Analisis Kompleksitas**

# #### **Merge Sort**
# - **Best Case, Worst Case, Average Case:** \( O(n \log n) \)  
#   Algoritma membagi array menjadi dua secara rekursif (\( \log n \)) dan membutuhkan waktu \( O(n) \) untuk menggabungkan hasilnya. Kompleksitas tidak bergantung pada urutan awal elemen.

# #### **Bubble Sort**
# - **Worst Case (Big O):** \( O(n^2) \)  
# - **Best Case (Big Θ):** \( O(n) \) (saat data sudah terurut dan hanya membutuhkan satu iterasi).  
# - **Average Case (Big Θ):** \( O(n^2) \)  
#   Algoritma memeriksa semua elemen secara berulang, sehingga kompleksitas berbanding kuadrat dengan jumlah elemen.


# IMPLEMENTASI MERGE_SORT
import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

x = random.sample(range(0, 1000), 100)

start_time = time.time()
merge_sort(x)
merge_sort_time = time.time() - start_time

print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
print(f"Sorted Data (Merge): {x}")


# IMPLEMENTASI BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

x = random.sample(range(0, 1000), 100)

start_time = time.time()
bubble_sort(x)
bubble_sort_time = time.time() - start_time

print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")
print(f"Sorted Data (Bubble): {x}")
