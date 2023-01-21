import matplotlib.pyplot as plt
import numpy as np
# print(matplotlib.__version__)
# x = np.array([0, 10])
# y = np.array([0, 250])

# plt.plot(x, y)
# plt.show()

# x = np.array([1, 8])
# y = np.array([3, 10])

# plt.plot(x, y)
# plt.show()
# x = np.array([1, 30])
# y = np.array([3, 10])

# plt.plot(x, y, "*")
# plt.show()
# x = np.array([1, 50])
# y = np.array([2, 40])
# plt.plot(x, y, '*')
# plt.show()
# x = np.array([1, 5, 12, 11])
# y = np.array([3, 9, 11, 20])

# plt.plot(x, y)
# plt.show()
# y = np.array([4, 8, 12, 11, 12, 11, 10])
# plt.plot(y)
# plt.show()
# y = np.array([4, 3, 5, 6, 7, 10])
# plt.plot(y, marker='*')
# plt.show()
# y = np.array([4, 8, 12, 11, 12])
# plt.plot(y, marker='*')
# plt.show()
# y = np.array([4, 8, 12, 11, 12])
# plt.plot(y, '*:g')
# plt.show()
# y = np.array([4, 8, 12, 11, 12])
# plt.plot(y, linestyle='dashed')
# plt.show()

# y1 = np.array([1, 8, 12, 11])
# y2 = np.array([3, 9, 11, 9])

# plt.plot(y1, marker='o')
# plt.plot(y2, marker='*')

# plt.xlabel("samping")
# plt.ylabel("atas")
# plt.show()

x = np.array([1, 8, 12, 11, 12, 14, 16])
y = np.array([3, 9, 11, 9, 11, 14, 16])

# font1 = {'family': 'serif', 'color': 'red', "size": 20}
# font2 = {'family': 'serif', 'color': 'blue', "size": 15}
# plt.title("Judul", fontdict=font1)
# plt.xlabel("samping", fontdict=font1)
# plt.ylabel("atas", fontdict=font2)
# plt.plot(x, y)


# plt.show()
# x = np.array([1, 8, 12, 11, 12, 14, 16])
# y = np.array([3, 9, 11, 9, 11, 14, 16])

# font1 = {'family': 'serif', 'color': 'green', "size": 20}
# font2 = {'family': 'serif', 'color': 'blue', "size": 15}
# plt.title("Judul", fontdict=font1)
# plt.xlabel("samping", fontdict=font1)
# plt.ylabel("atas", fontdict=font2)
# plt.plot(x, y)

# plt.grid()

# plt.show()

x = np.array([1, 8, 12, 11])
y = np.array([3, 9, 11, 9])

plt.subplot(1, 2, 1)
plt.plot(x, y)

x = np.array([1, 8, 12, 11])
y = np.array([3, 6, 9, 10])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()
# x = np.array([1, 8, 12, 11])
# y = np.array([3, 9, 11, 9])

# plt.subplot(2, 1, 1)
# plt.plot(x, y)

# x = np.array([1, 8, 12, 11])
# y = np.array([3, 6, 9, 10])

# plt.subplot(2, 1, 2)
# plt.plot(x, y)

# plt.show()
# x = np.array([1, 8, 12, 11, 12, 14, 11, 16, 13, 14, 12])
# y = np.array([3, 9, 11, 9, 12, 14, 15, 11, 12, 14, 11])
# plt.scatter(x, y)

# x = np.array([1, 8, 12, 11, 12, 14, 11, 11, 13, 14, 11])
# y = np.array([3, 6, 9, 10, 12, 14, 15, 11, 14, 16, 20])
# plt.scatter(x, y)

# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 9, 11, 9])
# plt.bar(x, y)
# plt.show()


# x = np.random.normal(170, 20, 250)
# plt.hist(x)
# plt.show()
# y = np.array([3, 9, 11, 9])
# mylabels = ["mobil", "motor", "rumah", "HP"]
# plt.pie(y, labels=mylabels, startangle=90)
# plt.show()
