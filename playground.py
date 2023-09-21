#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import tools

sample_rate, samples_B = tools.read_wav_file('oldstreet-0-2.wav')

print(sample_rate)

frame_rfft_B = tools.frame_rfft(samples_B, 1024, 0)

amplitude_B = np.abs(frame_rfft_B)

radians_B = np.angle(frame_rfft_B)

plt.imshow(amplitude_B[:,:64].T, cmap='viridis', origin='lower', aspect='auto')
plt.show()


