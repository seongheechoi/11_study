import arlpy
import matplotlib.pyplot as plt

# t = arlpy.signal.time(100000, fs=25000)
# print(t)
# print(len(t))
x = arlpy.signal.sweep(10, 20, duration=0.5, fs=1000)
print(x)
print(len(x))
plt.plot(x)
plt.show()