import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)
unit_step = np.where(n >= 0, 1, 0)
ramp = np.where(n >= 0, n, 0)
a = 1.1
expo = a ** n
f = 0.1
sine = np.sin(2 * np.pi * f * n)
cosine = np.cos(2 * np.pi * f * n)

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.stem(n, unit_step)
plt.title("Unit Step Function")

plt.subplot(3, 2, 2)
plt.stem(n, ramp)
plt.title("Ramp Function")

plt.subplot(3, 2, 3)
plt.stem(n, expo)
plt.title(f"Exponential Function (a={a})")

plt.subplot(3, 2, 4)
plt.stem(n, sine)
plt.title(f"Sine Function (f={f})")

plt.subplot(3, 2, 5)
plt.stem(n, cosine)
plt.title(f"Cosine Function (f={f})")

plt.tight_layout()
plt.show()
