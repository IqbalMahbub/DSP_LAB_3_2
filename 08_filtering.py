import numpy as np
import matplotlib.pyplot as plt

# Example input signal
x = np.array([1, 3, 4, 6, 7, 8, 10, 12, 11, 9, 8, 7, 5, 3, 2])

x_pad=np.concatenate((np.zeros(6),x))

y_avg=np.zeros(len(x))
y_diff= np.zeros(len(x))

for n in range(5,len(x)):
    y_avg[n]=(1/6)*np.sum(x[n-5:n+1])

for n in range(len(x)):
    if n>=6:
        y_diff[n]=x[n]-x[n-6]
    else:
        y_diff[n]=0

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.stem(x)
plt.title('Oriinal signal')
plt.grid(True)



plt.subplot(3,1,2)
plt.stem(y_avg)
plt.title('avaraging filter')
plt.grid(True)

plt.subplot(3,1,3)
plt.stem(y_diff)
plt.title('Diffanrce filter')
plt.grid(True)

plt.tight_layout()
plt.show()
