"""
Numpy: yüksek performanslı sayısal hesap kütüphanesi
    - büyük veri, hızlı matematik, matris hesaplamaları, bilimsel ve istatistiksel işlem
    - numpy C dili ile yazılmıştır

Numpy neden gerekli?
    - daha hızlı hesaplama
    - çok boyutlu veri yapıları
        - matrisler, N boyutlu dizi ile veri tabloları
    - matematiksel işlem kolaylığı

Numpy ve Yapaz Zeka
    - Scikit-learn (ml)
    - tensorflow ve pytorch (dl)
    - pandas (data science)

Numpy bölümünde ne öğreneceğiz?
    - Diziler
    - matematiksel işlemler
    - indeksleme ve dilimleme
    - dizi birleştirme ve bölme
    - çok boyutlu diziler
    - matris işlemleri
    - rastgele sayı üretimi

"""

import numpy as np

"""
Diziler (array)
    - ndarray: n-dimensional array
"""

# liste ile numpy dizisi arasındaki fark

sayilar = [1, 2, 3, 4, 5] # liste
print(sayilar)

# np.array() => python listesini numpy arrayine dönüştürür
dizi = np.array(sayilar) # numpy dizisi
print(dizi)   # [1 2 3 4 5]

# numpy dizisi tipini inceleme
print(type(dizi))  # <class 'numpy.ndarray'>

# numpy dizisi boyutu öğrenme
print(dizi.shape)  # (5,) -> 5 elemanlı tek boyutlu bir dizi

# numpy dizisinin veri tipi
print(dizi.dtype)  # int64 -> integer

# numpy ile dizi oluşturmanın farklı yollarına
dizi = np.zeros(5)  # [0. 0. 0. 0. 0.]
print(dizi)

dizi = np.ones(5)  # [1. 1. 1. 1. 1.]
print(dizi)

# belirli bir aralıkta sayı dizisi oluşturma
dizi = np.arange(0, 10) 
print(dizi) # [0 1 2 3 4 5 6 7 8 9]  0'dan başlar 10'a kadar sayıları üretir

# belirli aralıklarla sayı üretme
dizi = np.arange(0, 10, 2)
print(dizi) # [0 2 4 6 8]

# belirli bir aralığa eşit bölünmüş diziler
dizi = np.linspace(0, 10, 5) # 0 ile 10 arasında 5 sayı üret
print(dizi)  # [ 0.   2.5  5.   7.5 10. ]

"""
matematiksel işlemler 
"""

# toplama: z = a0 + a1w1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sonuc = a + b
print(sonuc) # [5 7 9]

# çıkarma
sonuc = a - b
print(sonuc) # [-3 -3 -3]

# çarpma
sonuc = a * b
print(sonuc) # [ 4 10 18]

# bölme
sonuc = a / b
print(sonuc) # [0.25 0.4  0.5 ]

# dizi ile sayı arasında işlem yapma
a = np.array([1, 2, 3])
sonuc = a * 2
print(sonuc) # [2 4 6]

# dizinin karesini almak
a = np.array([1, 2, 3, 4])
sonuc = a ** 2
print(sonuc) # [ 1  4  9 16]

# karekökünü alma mse -> rmse
a = np.array([1, 4, 9, 16])
sonuc = np.sqrt(a)
print(sonuc) # [1. 2. 3. 4.]

# dizinin toplamını bulma
a = np.array([1, 2, 3, 4])
print(np.sum(a)) # 10

# ortalama
print(np.mean(a)) # 2.5

# min ve max değerler
print(np.max(a)) # 4
print(np.min(a)) # 1

# standart sapma
print(np.std(a)) # 1.1

"""
indeksleme (indexing) - dilimleme (slicing)
"""

# dizilerde indeksleme
dizi = np.array([10, 20, 30, 40, 50])
print(dizi[0]) # dizinin ilk elemanına 0 indeksi ile erişmiş olurum
print(dizi[1])

# negatif indeksleme
print(dizi[-1]) # 50

# slicing (dilimleme)
# genel kullanım: dizi[başlangıç:bitiş]
print(dizi[1:4]) # [20, 30, 40]  1. indeksten başlar 4. indekse kadar gider fakat 4 dahil değildir

# baştan dilimleme
print(dizi[:3]) # [10 20 30]

# sondan dilimleme
print(dizi[2:]) # [30 40 50]

# adım (step) kullanımı
print(dizi[::2]) # diziden ikişer adım ile eleman seçmek # [10 30 50]

# 2 boyutlu dizilerde indeksleme
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris[0,0]) # 1

# belirli bir satırı seçmek
print(matris[1, :]) # [4 5 6]

# belirli bir sütunu seçmek
print(matris[:,2]) # [3 6 9]

# matris dilimleme   # keşisen kümeler
print(matris[0:2, 0:2])

matris_deneme = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
)

print(matris_deneme)

print(matris_deneme[0,0]) # 1
print(matris_deneme[0,1]) # 2
print(matris_deneme[0,2]) # 3
print(matris_deneme[1,0]) # 4
print(matris_deneme[1,1]) # 5
print(matris_deneme[1,2]) # 6
print(matris_deneme[2,0]) # 7
print(matris_deneme[2,1]) # 8
print(matris_deneme[2,2]) # 9
print(matris_deneme[3,0]) # 10
print(matris_deneme[3,1]) # 11
print(matris_deneme[3,2]) # 12

print(matris_deneme[0, :]) # [1 2 3]
print(matris_deneme[1, :]) # [4 5 6]
print(matris_deneme[2, :]) # [7 8 9]

print(matris_deneme[:, 0]) # [ 1  4  7 10]
print(matris_deneme[:, 1]) # [ 1  4  7 10]
print(matris_deneme[:, 2]) # [ 1  4  7 10]

print(matris_deneme[0:2, 0:2])
print(matris_deneme[1:2, 1:2]) # [[5]]

"""
Dizi birleştirme ve bölme
"""

# dizi birleştirme
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a, b))
print(sonuc) # [1 2 3 4 5 6]

# iki boyutlu dizi birleştirme
a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.concatenate((a, b))
print(sonuc)
"""
varsayılan olarak satır yönünde birleştirdik
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# axis parametresi
# axis = 0 -> satır yönünde birleştirme
# axis = 1 -> sütun yönünde birleştirme

sonuc = np.concatenate((a, b), axis= 1)
print(sonuc)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""

# vstack (dikey birleştirme): axis = 0 gibi yapar
sonuc = np.vstack((a, b))
print(sonuc)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# hstack (yatay birleştirme): axis = 1 gibi yapar
sonuc = np.hstack((a, b))
print(sonuc)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""

# diziyi parçalara bölme
dizi = np.array([1, 2, 3, 4, 5, 6])

sonuc = np.split(dizi, 2) # 2 parçaya böl
print(sonuc) # [array([1, 2, 3]), array([4, 5, 6])]

sonuc = np.split(dizi, 3) # 3 parçaya böl
print(sonuc) # [array([1, 2]), array([3, 4]), array([5, 6])]

# iki boyutlu dizilerde bölme
matris = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.split(matris, 2) # satır bazında 2 ye bölme
print(sonuc)
"""
[array([[1, 2],
       [3, 4]]), 
       
array([[5, 6],
       [7, 8]])]
"""

sonuc = np.split(matris, 2, axis=1) # sütun bazında 2 ye bölme
print(sonuc)
"""
[array([[1],
       [3],
       [5],
       [7]]), 
array([[2],
       [4],
       [6],
       [8]])]
"""

"""
çok boyutlu diziler
"""

# iki boyutlu dizi oluşturma
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# dizinin boyutunu öğrenme
print(matris.shape) # (3, 3)

# dizinin kaç boyutlu olduğunu öğrenmek
print(matris.ndim) # 2

# dizideki eleman sayısı
print(matris.size) # 9

# 3 boyutlu dizi oluşturma
"""
görsel -> (height, width) -> (yükseklik ve genişlik) -> (1920, 1080), (1920, 1080), (1920, 1080), ... (1920, 1080) -> (N, 1920, 1080)
"""

dizi3 = np.array(
    [
       [
           [1, 2],
           [3, 4]
           
       ],
       [
           [5, 6],
           [7, 8]
           
       ]
    ]
)
print(dizi3)
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""

"""
(2 adet matris, her matriste 2 satır, her matriste 2 satır)
"""
print(dizi3.shape) # (2, 2, 2)

# numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(12)
print(dizi) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# matrise dönüştürme
matris = dizi.reshape(3, 4)
print(matris)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

# matris= dizi.reshape(3, 5)
# print(matris) # ValueError: cannot reshape array of size 12 into shape (3,5)


"""
matris işlemleri
"""

# matris oluşturma
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a)
print(b)

print(a + b) # toplam
print(a - b) # çıkarma
print(a * b) # çarpma

# gerçek matris çarpımı
sonuc = np.dot(a, b)
print(sonuc)

"""
[1, 2],
[3, 4]
*
[5, 6],
[7, 8]
=
[[19 22]
 [43 50]]
"""

# matris transpose (matrisin ters çevrilmesi) satır sütuna çevrilir
print(a.T)

"""
[1, 2],
[3, 4]

[[1 3]
 [2 4]]
"""

# matris determinantı
det = np.linalg.det(a)
print(det) # -2.0000000000000004

# matrisin tersi
ters = np.linalg.inv(a)
print(ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]]
"""
"""
rastgele sayı üretme
"""

# rastgele ondalık sayılar üretme [0-1] arasında
rastgele = np.random.rand(5)
print(rastgele) # [0.06981736 0.7557126  0.17012666 0.17501852 0.00989046]

# rastgele matris oluşturma
rastgele = np.random.rand(3, 3)
print(rastgele)
"""
[[4.61652770e-01 1.46585306e-04 9.64485000e-01]
 [1.59860695e-01 4.11408491e-01 3.72743888e-01]
 [4.15557466e-01 8.69743714e-01 3.24127922e-01]]
"""

# rastgele tam sayı üretme
rastgele = np.random.randint(1, 10, 5) # 1 ile 10 arasında 5 adet rastgele tam sayı üret
print(rastgele) # [6 4 4 5 7]

# rastgele tam sayı matrisi üretme
rastgele = np.random.randint(1, 20, (3, 4)) # 1 ile 20 arasında 3 satır 4 sütundan oluşan 12 tane tam sayı üret
print(rastgele)
"""
[[14  2 10 15]
 [18 11 13  6]
 [ 3  4 10  4]]
"""

# aynı rastgele sonucu üretmek için (seed)
np.random.seed(42)
rastgele = np.random.rand(5)
print(rastgele) # [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]

# bir diziden rastgele eleman seçmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

# birden fazla eleman seçme
secim = np.random.choice(dizi, 3)
print(secim)