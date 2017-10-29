# Created by: Vivian Le
# Created: 10/28/17
# Last Modified: 10/28/17
# Purpose: Hackathon Project (BostonHacks 2017) - TermDoggo

import pyaudio
import wave

#Takes user voice commands and translate it to a string
def speech():
	FORMAT = pyaudio.paInt32
	RATE = 44000
	CHANNELS = 2
	CHUNK = 1000
	TIME = 5		#seconds

	record = pyaudio.PyAudio()

	stream = record.open(format = FORMAT, channels = CHANNELS ,rate = RATE,
			 input = True, frames_per_buffer = CHUNK)

	frames = []

	for i in range(0, int(RATE / CHUNK * TIME)):
		data = stream.read(CHUNK)
		frames.append(data)

	stream.stop_stream()
	stream.close()
	record.terminate()

	wavef = wave.open("command.wav", 'wb')
	wavef.setnchannels(CHANNELS)
	wavef.setsampwidth(record.get_sample_size(FORMAT))
	wavef.setframerate(RATE)
	wavef.writeframes(b''.join(frames))
	wavef.close()

#def convo():

def lazy():
	print("Nah (in french).")

def main():
	speech()

if __name__ == '__main__':
    main()