import numpy as np
import matplotlib.pyplot as plt

fs=1000
t=np.arange(0,1,1/fs)
signal_clean = np.sin(2*np.pi*50*t)
noise = 0.5*np.sin(2*np.pi*300*t)
signal_noisy= signal_clean+noise

N=15
h=np.ones(N)/N