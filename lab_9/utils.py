import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import librosa
from scipy.io import wavfile
import soundfile as sf


def get_spectrogram(filename):
    audio, sr = librosa.load(filename, sr=None)
    window_size = 4096
    hop_length = int(window_size / 4)
    n_fft = window_size
    spectrogram = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length, window=signal.hann(window_size))
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
    plt.figure(figsize=(12, 5))
    librosa.display.specshow(spectrogram_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    return plt


def savgol_test():
    sample_rate, data = wavfile.read('smokeonthewater.wav')
    data = data.astype(float)
    window_length = 51
    polyorder = 3
    filtered_data = signal.savgol_filter(data, window_length, polyorder)
    filtered_data = filtered_data.astype('int16')
    wavfile.write('smokeonthewater_savgol_filter.wav', sample_rate, filtered_data)


def add_noise():
    audio, sr = librosa.load('smokeonthewater.wav', sr=None)
    RMS = np.sqrt(np.mean(audio ** 2))
    STD_n = 0.001
    noise = np.random.normal(0, STD_n, audio.shape[0])
    audio_noise = audio + noise
    sf.write('smokeonthewater_with_noise.wav', audio_noise, sr)


def savgol_test_noise():
    sample_rate, data = wavfile.read('smokeonthewater_with_noise.wav')
    data = data.astype(float)
    window_length = 51
    polyorder = 3
    filtered_data = signal.savgol_filter(data, window_length, polyorder)
    filtered_data = filtered_data.astype('int16')
    wavfile.write('smokeonthewater_with_noise_savgol_filter.wav', sample_rate, filtered_data)


# ORIGINAL
spectrogram_original = get_spectrogram("smokeonthewater.wav")
spectrogram_original.savefig('spectrogram_original.png')

# SAVGOL FILTER
savgol_test()
spectrogram_savgol_filter = get_spectrogram("smokeonthewater_savgol_filter.wav")
spectrogram_savgol_filter.savefig('spectrogram_savgol_filter.png')

# ORIGINAL NOISE
add_noise()
spectrogram_noise = get_spectrogram("smokeonthewater_with_noise.wav")
spectrogram_noise.savefig("spectrogram_noise.png")

# SAVGOL FILTER NOISE
savgol_test_noise()
spectrogram_noise_via_savgol = get_spectrogram("smokeonthewater_with_noise_savgol_filter.wav")
spectrogram_noise_via_savgol.savefig("spectrogram_noise_savgol.png")
