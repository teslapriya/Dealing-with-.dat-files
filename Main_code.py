import numpy as np 
import os

# Reading .dat files
path = '/home/user/grex/pipeline/fake/simulated_frb_dm200.00_fluence35.00.dat'

def read_file(path):
    return np.fromfile(path, dtype=np.int8)

def reduce_amplitude(amplitude, factor):
    return (amplitude/factor).astype(np.int8)

def save_file(path, amplitude):
    data.tofile(file_path)

amplitude = read_file(path)

non_zero_indices = np.nonzero(amplitude)[0]

for index in non_zero_indices:
    print(f"Index: {index}, Amplitude: {amplitude[index]}")

# Reduce the Amplitude of pulses
reduced_amp = reduce_amplitude(amplitude, np.sqrt(2))

for index in non_zero_indices:
    difference = amplitude[index] - reduced_amp[index]
    print(f"Index: {index}, Difference: {difference}")   

# Implement and save to all files
for filename in os.listdir(path):
    if filename.endswith(".dat"):  
        file_path = os.path.join(path, filename)
        
        data = read_file(file_path)
        
        reduced_amp = reduce_amplitude(amplitude, np.sqrt(2))
    
        save_file(file_path, reduced_amp)
        
        print(f"Modified and saved: {filename}")  