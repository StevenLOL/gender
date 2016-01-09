import sys
import scipy.io.wavfile
import wave
import struct
import numpy as np
from itertools import chain

def readWaveFile(fileName):
    waveFile = wave.open(fileName,'r')
    channels = waveFile.getnchannels()
    sampwidth = waveFile.getsampwidth()
    framesNumber = waveFile.getnframes()
    framerate = waveFile.getframerate()
    frames = waveFile.readframes(framesNumber)
    data = struct.unpack("%dh" %  channels*framesNumber, frames)
    oneChannelData = data[::channels]
    oneChannelData = list(chain(oneChannelData))
    waveFile.close()
    return data, channels, sampwidth, framerate, framesNumber

fileName = sys.argv[1]
data, channels, sampwidth, framerate, framesNumber = readWaveFile(fileName)
time = framesNumber / framerate
print (channels)
print (sampwidth)
print (framerate)
print (framesNumber)
print (time)

dataFFT = np.fft(data)
absDataFFT = abs(dataFFT)
maxAmplitude = np.amax(dataFFT)


# if (waveFile.getnchannels()>1):
#     speech = waveFile[0]
# length = waveFile.getnframes()
# load_wav(fileName,samplerate=44100)
# files = ['train/002_M.wav','train/003_K.wav','train/004_M.wav','train/005_M.wav',
#          'train/006_K.wav','train/007_M.wav','train/008_K.wav','train/009_K.wav','train/010_M.wav',
#          'train/014_K.wav','train/015_K.wav',
#          'train/016_K.wav','train/017_M.wav','train/018_K.wav','train/019_M.wav','train/020_M.wav',
#          'train/021_M.wav','train/022_K.wav','train/023_M.wav','train/024_M.wav','train/025_K.wav',
#          'train/026_M.wav','train/027_M.wav','train/028_K.wav','train/029_K.wav','train/030_M.wav',
#          'train/031_K.wav','train/032_M.wav','train/033_M.wav','train/034_K.wav','train/035_M.wav',
#          'train/036_K.wav','train/037_K.wav','train/038_M.wav','train/039_M.wav','train/040_K.wav',
#          'train/041_K.wav','train/042_M.wav','train/043_M.wav','train/044_K.wav','train/045_M.wav',
#          'train/046_K.wav','train/047_K.wav','train/048_K.wav','train/049_M.wav','train/050_K.wav',
#          'train/051_K.wav','train/052_M.wav','train/053_M.wav','train/054_K.wav','train/055_K.wav',
#          'train/056_M.wav','train/057_K.wav','train/058_M.wav','train/059_K.wav','train/060_K.wav',
#          'train/061_M.wav','train/062_K.wav','train/063_M.wav','train/064_M.wav','train/065_M.wav',
#          'train/066_K.wav','train/067_K.wav','train/068_K.wav','train/069_K.wav','train/070_M.wav',
#          'train/071_M.wav','train/072_K.wav','train/073_K.wav','train/074_K.wav','train/075_M.wav',
#          'train/076_M.wav','train/077_K.wav','train/078_M.wav','train/079_K.wav','train/080_M.wav',
#          'train/081_K.wav','train/082_M.wav','train/083_K.wav','train/084_M.wav','train/085_K.wav',
#          'train/086_K.wav','train/087_M.wav','train/088_K.wav','train/089_M.wav','train/090_M.wav',
#          'train/091_M.wav',]

# ok = 0
# error = 0
#
# for i in files:
#     try:
#         w, signal = scipy.io.wavfile.read(i)
#     except:
#         error = error+1
#         print("Error in opening file"+i)
#     else:
#         ok=ok+1

# w, signal = scipy.io.wavfile.read(fileName)

# print (ok)
# print (error)
# channels = signal.getnchannels()
# if (channels>1):
#     signal = signal[:, 0]
#     samples_count = len(signal)
#     duration = float(samples_count) / w
#
#     print(samples_count)
#     print(duration)