#############################################
# NUMPY
############################################

# Neden NumPy (Why Numpy)

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b
# numpy python'da numeric işlemler için geliştirilmiş bir kütüphanedir.
# numpy listelere göre daha hızlıdır. Çünkü sabit tipte veri tutar. Yani verimli veri saklar.
# Yüksek seviyeden işlem açıp kapatır. Vektör seviyesinde işlem yapar.

# NumPy Array'i Oluşturmak(Creating NumPy Arrays)
import numpy as np
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5])) # ndarray

np.zeros(10, dtype=int) # girdiğin sayı adedince sıfırlardan oluşan array oluşturur.
np.random.randint(0, 10, size=10) # 0 ile 10 arasında 10 tane random array oluşturur.
np.random.normal(10, 4, (3, 4)) # ortalması 10 standart sapması 4 3'e 4lük bir array oluştur.

# NumPy Array Özellikleri (Attibutes of numpy Arrays)

import numpy as np

a = np.random.randint(10, size=5)
a.ndim # boyut sayısı
a.shape # boyut bilgisi
a.size # toplam eleman sayısı
a.dtype # array veri tipi

# Yeniden Şekillerndirme(Reshaping)

import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

# Index Seçimi (Index Selection)

a = np.random.randint(10, size=10)
a[0]
a[0:5] #slicing
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0] # satır, sütun
m[1 ,1]
m[2, 3] = 999
m[2 , 3] = 2.9 # 2.9 ondalık değerini 2 olarak dahil eder.
m[:, 0] # tüm satırları seç , sıfırıncı sütunu seç
m[1, :] # birinci satır, tüm sütunlar
m[0:2, 0:3] # satırlarda 0'dan başla 2'ye kadar git, sütunlarda 0'dan başla 3'e kadar git

# Fancy Index

v = np.arange(0, 30, 3) # 0'dan 3'a kadar 3'er 3'er oluşturulmuş array
v[1]
v[4]

catch = [1, 2, 3]
v[catch]
v[[1 ,2, 3]]

# Numpy'da Koşullu İşlemler(conditions on numpy)

v = np.array([1, 2, 3, 4, 5])

ab = []

for i in v:
    print(i)

for i in v:
    if i < 3:
        ab.append(i)
v < 3
v[v < 3]
v[v > 3]
v[v == 3]
v[v != 3]
v[v >= 3]

# Matematiksel işlemler(Mathematical Operations)

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
v = np.subtract(v, 1)

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]]) # birinci değişkesin katsayıları, ikinci değişkenin katsayıları
b = np.array([12, 10]) # sonuçlar

np.linalg.solve(a, b)


# Sabit tipte veriler tutar her biri için tip, boyut bilgisi tutmaz ve yüksek seviyeden vektörel işlemler yapabilir, hızlıdır.

