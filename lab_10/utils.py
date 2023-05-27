import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import librosa


def get_spectrogram(filename):
    audio, sr = librosa.load(filename, sr=None)

    window_size = 2048  # Size of the window for the STFT
    hop_length = int(window_size / 4)  # Hop size between consecutive windows
    n_fft = window_size

    spectrogram = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length, window=signal.hann(window_size))
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(12, 5))
    librosa.display.specshow(spectrogram_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram {filename}')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    return plt


def get_min_max_speech_freq(audio_file):
    sample_rate, audio_data = wav.read(audio_file)
    spectrum = np.fft.fft(audio_data)
    amplitude_spectrum = np.abs(spectrum)
    fundamental_frequency = np.argmax(amplitude_spectrum)
    frequencies = np.fft.fftfreq(len(amplitude_spectrum), 1 / sample_rate)
    min_freq = frequencies[1]
    max_freq = frequencies[fundamental_frequency]
    return min_freq, max_freq



spectogram_A = get_spectrogram("A.wav")
spectogram_A.savefig('spectogram_AAA.png')

spectogram_I = get_spectrogram("I.wav")
spectogram_A.savefig('spectogram_III.png')

spectogram_GAV = get_spectrogram("GAVGAVGAV.wav")
spectogram_GAV.savefig('spectogram_GAV.png')

spectogram_MEOW = get_spectrogram("MEOW.wav")
spectogram_MEOW.savefig('spectrogram_MEOW.png')


audio_file = 'A.wav'
min_voice_freq, max_voice_freq = get_min_max_speech_freq(audio_file)

print('A')
print("Минимальная частота голоса:", int(min_voice_freq))
print("Максимальная частота голоса:", int(max_voice_freq))


print()
print('---------')
print()

audio_file = 'I.wav'
min_voice_freq, max_voice_freq = get_min_max_speech_freq(audio_file)

print('I')
print("Минимальная частота голоса:", int(min_voice_freq))
print("Максимальная частота голоса:", int(max_voice_freq))

print('GAV')
audio_file = 'GAVGAVGAV.wav'
min_voice_freq, max_voice_freq = get_min_max_speech_freq(audio_file)
print("Минимальная частота голоса:", int(min_voice_freq))
print("Максимальная частота голоса:", int(max_voice_freq))

print()
print('---------')
print()

print('MEOW')
audio_file = 'MEOW.wav'
min_voice_freq, max_voice_freq = get_min_max_speech_freq(audio_file)

print("Минимальная частота голоса:", int(min_voice_freq))
print("Максимальная частота голоса:", int(max_voice_freq))


