import time
import random
import matplotlib.pyplot as plt


# 🟢 Insertion Sort Algoritması
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 🟢 Zaman Ölçümü Fonksiyonu
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


# 🟢 Deneysel Analiz
dizi_boyutlari = [100, 500, 1000, 2000, 5000, 10000]
zamanlar = []

print("📌 Insertion Sort Performans Testi")
for size in dizi_boyutlari:
    test_array = [random.randint(0, 10000) for _ in range(size)]

    # 🕒 Insertion Sort Çalışma Süresi
    insertion_time = measure_time(insertion_sort, test_array.copy())

    print(f"Dizi Boyutu: {size} - Süre: {insertion_time:.6f} saniye")
    zamanlar.append(insertion_time)

# 🟢 Grafik Çizdirme
plt.plot(dizi_boyutlari, zamanlar, marker='o', linestyle='-', color='r', label="Insertion Sort")
plt.xlabel("Dizi Boyutu")
plt.ylabel("Çalışma Süresi (saniye)")
plt.title("Insertion Sort Zaman Karmaşıklığı")
plt.legend()
plt.grid(True)
plt.show()
