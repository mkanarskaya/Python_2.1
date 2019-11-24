import numpy as np
import string
#import scipy as sc
data = []
with open("data.txt") as f:
    b = f.read()
    b = b.split("\n")
    for i in range(len(b)):
        b[i] = int(b[i])
a = np.array(b)
print("Array: ", a)
print("Mean: ", a.mean(), ", max: ", a.max(), ", min: ", a.min(), ", RMS: ", np.std(a))
real_int = np.random.randint(-100, 100, 15)
print(np.sort(real_int))
real = np.random.randint(-100, 100, 20)
image = np.random.randint(-100, 100, 20)*1j
complex_array = real + image
print("sorted array of complex by abs: ", sorted(complex_array, key = abs))
print("sorted array of real: ", np.sort(real)[::-1])
#сортировка строк
rand_str = [''.join([np.random.choice(list(string.ascii_letters)) for i in range(np.random.randint(1,10))]) for j in range(20)]
str_array = np.array(rand_str)
print(str_array)
print(sorted(str_array, key = len))
print (sorted(str_array))




