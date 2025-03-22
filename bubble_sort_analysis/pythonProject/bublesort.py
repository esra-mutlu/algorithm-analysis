import time
import random
import matplotlib.pyplot as plt


# 🟢 Bubble Sort Algoritması
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 🟢 Zaman Ölçümü Fonksiyonu
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


# 🟢 Deneysel Analiz
dizi_boyutlari = [100, 500, 1000, 2000, 5000, 10000]
zamanlar = []

print("📌 Bubble Sort Performans Testi")
for size in dizi_boyutlari:
    test_array = [random.randint(0, 10000) for _ in range(size)]

    # 🕒 Bubble Sort Çalışma Süresi
    bubble_time = measure_time(bubble_sort, test_array.copy())

    print(f"Dizi Boyutu: {size} - Süre: {bubble_time:.6f} saniye")
    zamanlar.append(bubble_time)

# 🟢 Grafik Çizdirme
plt.plot(dizi_boyutlari, zamanlar, marker='o', linestyle='-', color='b', label="Bubble Sort")
plt.xlabel("Dizi Boyutu")
plt.ylabel("Çalışma Süresi (saniye)")
plt.title("Bubble Sort Zaman Karmaşıklığı")
plt.legend()
plt.grid(True)
plt.show()
