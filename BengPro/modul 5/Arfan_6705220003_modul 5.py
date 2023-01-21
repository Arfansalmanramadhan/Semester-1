from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd

# a = np.array([[1, 2, 3, 4, 5, ], [10, 11, 12, 13, 14]])
# print(a)
# print(type(a))
# print(a[0, 4])
# ary = np.array([[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]])
# print(ary)
# print(type(ary))
# print(ary[0, 4])

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5, ])
# c = np.array([[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]])
# d = np.array([[[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]])
# e = np.array([[[[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]]])
# f = np.array([[[[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# print(e.ndim)

# A = np.array([1, 2, 3, 4, 5, ])
# B = np.array([5, 5, 5, 5, 5, ])
# print("Penjumlahan =", A + B)
# print("Pengurangan =", A - B)
# print("Pmbagian =", A / B)
# print("Perkalin =", A * B)
# print("Perpangkatan =", A ** B)
# C = np.array([1, 2, 3, 4, 5, ])
# print("Nilai minimal =", C.min())
# print("Nilai Maksimal =", C.max())
# print("Nilai rata-rata =", C.mean())
# print("Total niai =", C.sum())
# print(C.zeros())


pd.read_csv("data.csv")
# print(df)
df = pd.read_csv("data.csv")
print(df.to_string())
dict = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika"],
        "ibu kota": ["Jakarta", "Tokyo", "New Delhita", "Beijing", "Washingtong"],
        "luas": [1905, 377972, 3287, 9834, 12345],
        "popurlasi": [264, 143, 1253, 5298, 2345]}

# z = pd.DataFrame(dict)
# print(z)
# f = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
# print(csr_matrix(f).data)
# print(csr_matrix(f).count_nonzero())
# print(csr_matrix(f).count_nonzero())
b = pd.DataFrame(dict)
print(b)
