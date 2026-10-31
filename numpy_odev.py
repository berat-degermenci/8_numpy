# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

import numpy as np

dizi = np.arange(1, 21)
print(dizi) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
print(dizi.size) # 20


# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

dizi = np.array([5, 10, 15, 20, 25])
sonuc = dizi * 3
print(sonuc) # [15 30 45 60 75]


# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

dizi = np.arange(0, 31)
print(dizi)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30]

print(dizi[10:21]) # [10 11 12 13 14 15 16 17 18 19 20]

# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a, b))
print(sonuc) # [1 2 3 4 5 6]

# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

dizi = np.arange(1, 13)
matris = dizi.reshape(3, 4)

print(matris)
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
print(matris.shape) # (3, 4)

# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print(matris[1,:]) # [4 5 6]
print(matris[:,1]) # [2 5 8]

# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

rastgele = np.random.rand(3, 3)
print(rastgele)
"""
[[0.44116827 0.03357001 0.00294213]
 [0.7329021  0.45417338 0.23841521]
 [0.52518727 0.55936747 0.34705141]]
"""
print(np.mean(rastgele)) # 0.37053080397328864
print(np.max(rastgele)) # 0.732902101513865

# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

sonuc = a * b
print(sonuc) # [ 2 12 30 56]

# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

dizi = np.arange(1, 10)

matris = dizi.reshape(3, 3)
print(matris)

transpose = matris.T

print(matris)
print(transpose)

"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 4 7]
 [2 5 8]
 [3 6 9]]
"""

# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

rastgele = np.random.randint(1, 51, 10)
print(rastgele)

print(np.sum(rastgele)) # 255

print(np.mean(rastgele)) # 19.8