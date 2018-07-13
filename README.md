# MicrophoneRNG
Made a random number generator using microphone input just to see if I could, works surprisingly well.

### SETUP ###
Written in Python 2.7
I know this works within my linux environment, wasn't able to get it working on my Win7 PC. 

Requires installation of pyaudio to work, you can either use pip to install libportaudio and then pyaudio, or follow the instructions below.

1 sudo apt-get install git

2 git clone http://people.csail.mit.edu/hubert/git/pyaudio.git

3 sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

4 sudo apt-get python-dev

5 sudo python pyaudio/setup.py install

### USE ###

The script accepts two arguments. The first is the number of audio samples you want to collect, each sample becomes one random number. The second argument is the range you want the random number to fall within. All numbers will be returned as an integer.

The script will print out a list containing the TODO. As well as the average and standard deviation of all the random numbers. Since this was just a fun exercize, I just wanted to show to myself that the numbers were actually random.

### ISSUES ###

If your console is getting spammed with errors you just need to goto /usr/share/alsa/alsa.conf and comment out these three lines:
  pcm.rear cards.pcm.rear
  pcm.center_lfe cards.pcm.center_lfe
  pcm.side cards.pcm.side
I only have my linux environment setup for development so don't know where alsa.conf would be on a windows machine.

### TODO ###
