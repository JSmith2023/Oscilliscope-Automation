import numpy as np
import matplotlib.pyplot as plt

def filter_frequency_domain(data, sampling_rate, cutoff_frequency):
    # Perform Fourier Transform
    freq_data = np.fft.fft(data)
    
    # Determine the cutoff frequency bin
    cutoff_bin = int(cutoff_frequency / (sampling_rate / len(data)))

    # Apply Hamming window to taper the data to zero gradually
    window = np.hamming(2 * cutoff_bin)
    freq_data[:cutoff_bin] *= window[:cutoff_bin]
    freq_data[-cutoff_bin:] *= window[cutoff_bin:]

    # Perform Inverse Fourier Transform
    filtered_signal = np.fft.ifft(freq_data)

    return filtered_signal

def main():
    input_file = "10_perc_test_1.txt"  # Replace with the path to your input text file
    output_file = "output.txt"  # Replace with the path where you want to save the filtered data
    
    sampling_rate = 100e6  # 100 MHz (100 million samples per second)
    cutoff_frequency = 1e6  # 1 MHz (cutoff frequency for the filter)

    # Load data from the text file
    with open(input_file, 'r') as file:
        data_str = file.read().strip()

    # Convert the space-separated string of data to a NumPy array of ints
    data = np.array([int(value) for value in data_str.split()])

    # Apply frequency domain filtering
    filtered_signal = filter_frequency_domain(data, sampling_rate, cutoff_frequency)

    # Plot the original signal in the time domain
    time = np.arange(len(data)) / sampling_rate
    plt.subplot(2, 1, 1)
    plt.plot(time, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original Signal')

    # Compute FFT of the original signal
    freq_data = np.fft.fft(data)
    freq = np.fft.fftfreq(len(data), d=1/sampling_rate)
    
    # Plot the frequency domain representation of the original signal
    plt.subplot(2, 1, 2)
    plt.plot(freq, np.abs(freq_data))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain of Original Signal')
    plt.xlim(0, sampling_rate / 2)
    
    plt.tight_layout()
    plt.show()

    # Plot the filtered signal in the time domain
    time_filtered = np.arange(len(filtered_signal)) / sampling_rate
    plt.subplot(2, 1, 1)
    plt.plot(time_filtered, filtered_signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Filtered Signal')

    # Compute FFT of the filtered signal
    freq_filtered_data = np.fft.fft(filtered_signal)
    
    # Plot the frequency domain representation of the filtered signal
    plt.subplot(2, 1, 2)
    plt.plot(freq, np.abs(freq_filtered_data))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain of Filtered Signal')
    plt.xlim(0, sampling_rate / 2)
    
    plt.tight_layout()
    plt.show()

    # Save the filtered data to the output file
    with open(output_file, 'w') as file:
        for value in filtered_signal:
            file.write(str(value.real) + '\n')

if __name__ == "__main__":
    main()
