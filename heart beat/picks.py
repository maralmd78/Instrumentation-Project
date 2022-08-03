# -*- coding: utf-8 -*-
"""picks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgvCEXbWICKD7cxBICXdOvk5zD3R7DMZ
"""

!pip install numpy
!pip install neurokit2
!pip install pandas
!pip install matplotlib
!pip install matplotlib.pyplot
!pip install seaborn

import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from scipy.signal import butter, iirnotch, lfilter

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.rcParams['figure.figsize'] = [8, 5]  # Bigger images

# Retrieve ECG data from data folder (sampling rate= 1000 Hz)

temp = [-33, -31, -39, -41, -37, -31, -27, -19, -15, -13, -13, -25, -25, -25, -23, -25, -33, -23, -29, -23, -27, -27, -25, -35, -29, -25, -29, -29, -27, -33, -31, -19, -21, -15, -17, 5, 5, -5, -17, -23, -29, -25, -31, -41, -43, -43, -33, -33, -31, -123, -171, -37, 259, 515, 535, 489, 147, -83, -59, -57, -69, -73, -69, -61, -63, -61, -53, -47, -53, -49, -43, -39, -35, -37, -31, -25, -29, -25, -29, -31, -37, -35, -35, -33, -33, -23, -13, -19, -23, -15, -23, -31, -21, -25, -27, -25, -23, -21, -27, -27, -27, -29, -25, -23, -27, -27, -33, -31, -23, -17, -11, -11, -9, 13, 1, -3, -11, -23, -27, -27, -35, -41, -45, -35, -35, -31, -51, -175, -129, 129, 463, 585, 545, 245, -37, -55, -55, -57, -57, -67, -61, -57, -55, -55, -49, -49, -45, -39, -41, -33, -25, -27, -21, -23, -23, -19, -31, -33, -37, -37, -35, -39, -27, -21, -21, -19, -19, -23, -21, -23, -23, -25, -23, -23, -23, -23, -21, -21, -19, -25, -23, -21, -19, -21, -21, -21, -15, -9, -7, -5, 13, 3, -11, -19, -9, -19, -29, -31, -31, -37, -37, -33, -31, -31, -137, -169, 11, 329, 545, 571, 451, 99, -51, -43, -51, -59, -61, -67, -61, -69, -61, -53, -53, -53, -41, -43, -37, -33, -27, -31, -21, -25, -29, -27, -23, -35, -39, -43, -37, -37, -31, -25, -25, -27, -21, -25, -27, -33, -35, -35, -19, -25, -27, -29, -25, -23, -19, -25, -31, -25, -25, -33, -27, -23, -11, -7, -17, -9, 9, -1, -9, -25, -29, -23, -27, -35, -45, -41, -41, -49, -37, -39, -167, -155, 59, 417, 577, 529, 315, 1, -61, -53, -63, -71, -71, -73, -75, -67, -59, -57, -57, -53, -51, -49, -41, -35, -37, -29, -31, -35, -29, -43, -43, -43, -53, -49, -45, -35, -37, -35, -35, -35, -33, -35, -37, -41, -37, -37, -37, -33, -35, -39, -33, -37, -39, -33, -35, -35, -35, -37, -37, -39, -41, -25, -25, -29, -19, -5, -7, -15, -23, -29, -35, -43, -45, -47, -49, -51, -49, -47, -37, -145, -181, -21, 329, 523, 507, 365, 55, -69, -65, -67, -73, -75, -79, -75, -79, -71, -65, -69, -65, -57, -57, -51, -55, -59, -27, -37, -37, -37, -43, -43, -57, -59, -61, -45, -39, -31, -29, -35, -33, -41, -29, -37, -43, -43, -37, -39, -51, -37, -41, -45, -33, -31, -37, -41, -41, -43, -35, -37, -43, -37, -25, -25, -31, -19, 1, -13, -27, -29, -21, -33, -43, -45, -53, -47, -53, -55, -41, -65, -183, -139, 109, 431, 531, 475, 211, -43, -67, -69, -75, -73, -77, -79, -73, -75, -71, -65, -63, -55, -49, -47, -43, -45, -41, -39, -41, -37, -37, -41, -45, -43, -43, -51, -47, -37, -33, -29, -27, -31, -31, -29, -27, -31, -33, -33, -29, -33, -37, -29, -35, -27, -33, -27, -25, -27, -29, -29, -25, -27, -23, -15, -15, -19, 1, 15, -1, -11, -19, -15, -23, -29, -45, -35, -33, -39, -31, -27, -37, -149, -139, 95, 441, 559, 517, 283, -11, -59, -53, -59, -57, -57, -61, -59, -51, -55, -55, -45, -39, -37, -35, -31, -29, -29, -23, -27, -23, -21, -33, -29, -39, -33, -25, -29, -21, -11, -15, -15, -19, -13, -15, -21, -19, -17, -27, -25, -19, -23, -19, -23, -21, -21, -21, -33, -29, -13, -19, -19, -13, -3, -7, -5, 17, 3, -9, -17, -17, -21, -31, -31, -31, -37, -35, -35, -27, -61, -171, -91, 179, 491]
ecg_signal = pd.Series(temp)
# ecg_signal = pd.Series(np.random.uniform(-0.5,0.5,[50000]))

# Extract R-peaks locations
_, rpeaks = nk.ecg_peaks(ecg_signal, sampling_rate=128)

# Automatically process the (raw) ECG signal
signals, info = nk.ecg_process(ecg_signal, sampling_rate=128)

# Extract clean ECG and R-peaks location
rpeaks = info["ECG_R_Peaks"]
cleaned_ecg = signals["ECG_Clean"]

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, ecg_signal)
    return y

filtered_signal= butter_bandpass_filter(cleaned_ecg, 0.5, 50, 128, order=5)

plt.plot(filtered_signal)

# Visualize R-peaks in ECG signal
plot = nk.events_plot(rpeaks, filtered_signal)

# Plotting all the heart beats
epochs = nk.ecg_segment(filtered_signal, rpeaks=None, sampling_rate=250, show=True)

rr=nk.ecg_findpeaks(filtered_signal, sampling_rate=128, method='neurokit', show=True)

beat= (60*128)/(rr["ECG_R_Peaks"][1]-rr["ECG_R_Peaks"][0])

print(int(beat))