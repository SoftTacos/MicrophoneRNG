#!/usr/bin/env python

import pyaudio #YOU HAVE TO INSTALL THIS
import wave
import numpy
import sys, os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = .1

HUGE_PRIME = 15485863#one millionth prime number
SAMPLES = int(sys.argv[1])
RANGE = int(sys.argv[2])
results = []
sys.stderr = open(os.devnull, 'w')
for i in range(0, SAMPLES):
    audio = pyaudio.PyAudio()
    frames = []#array holding strings of bytes, the audio
    stream = audio.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    ### RECORDING ###
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    #concatenating frames into one array and converting each element of frames from bytes into integers
    data = numpy.frombuffer("".join(frames), dtype='B')

    ### HASHING ###
    randomized_audio = 0
    for i in range(0,len(data)):
        randomized_audio += data[i]# 3**(data[i])#simple way to 'numberize' the giant audio stream
    random_number = HUGE_PRIME * randomized_audio % RANGE
    
    results.append(random_number)
print results

frequencies = [0]*RANGE
for res in results:
    frequencies[int(res)]+=1
total = 0
for res in results:
    total+=res
average = total/SAMPLES
total_deviation = 0
for res in results:
    total_deviation+= abs(res-average)
std_dev = total_deviation/SAMPLES

print frequencies
print average
print std_dev
