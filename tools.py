import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def read_wav_file(filename: str) -> (float, np.ndarray[np.float64]):
    sample_rate, samples = wavfile.read(filename)
    if samples.dtype == np.int16:
        samples = samples / 32768.0
    if samples.dtype == np.int8:
        samples = samples / 128.0
    return float(sample_rate), samples.astype(np.float64)


def write_wav_file(
    filename: str,
    samples: np.ndarray[np.float64],
    sample_rate: float
) -> None:
    data = (samples * 32768.0).astype(np.int16)
    wavfile.write(filename, sample_rate, data)


def frame_count(
    sample_count: int,
    frame_size: int,
    overlap_size: int
) -> int:
    step_size = frame_size - overlap_size
    return int(np.floor(float(sample_count - overlap_size) / float(step_size)))


def frame_rfft(
    samples: np.ndarray[np.float64],
    frame_size: int,
    overlap_size: int
) -> np.ndarray[np.complex128]:
    wave_len = len(samples)
    step_size = frame_size - overlap_size
    frame_count = int(
        np.floor(float(wave_len - overlap_size) / float(step_size)))
    retval = np.zeros(
        (frame_count, int(np.ceil((frame_size + 1) / 2))),
        dtype=np.complex64)
    for i in range(frame_count):
        lmost = i * step_size
        rmost = lmost + frame_size
        frame = samples[lmost:rmost]
        retval[i, :] = np.fft.rfft(frame)
    return retval


def sin_wave(
    sample_rate: float,
    frequency: float,
    sample_count: int
) -> np.ndarray[np.float64]:
    time_array = np.arange(
        0, sample_count, dtype=np.float32) * 1.0 / sample_rate
    return np.sin(2 * np.pi * frequency * time_array)
