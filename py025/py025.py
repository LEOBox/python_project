#coding:utf-8
import webbrowser
import sys
import pyaudio
import wave
import BaiduVoiceTranslationAPI

sys.path.append('libs')

def record():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 16000
	RECORD_SECOND = 3
	WAVE_OUTPUT_FILENAME = 'output.wav'
	LANGUAGE = "zh"
	TPYE = 'wav'

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE,input = True,frames_per_buffer = CHUNK)

	print("*recording")

	frames = []
	for i in range(0,int(RATE / CHUNK*RECORD_SECOND)):
		data = stream.read(CHUNK)
		frames.append(data)

	print "DONE"

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME,'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	VoiceTranslation =  BaiduVoiceTranslationAPI.BaiduVoiceHttpClient('WlanFhHGsxkfzHeXhieXLGZk','eb8f5740df1b9a56696df2596ff8d068')
	VoiceRespone = VoiceTranslation.VocieTranslation(LANGUAGE,CHANNELS,WAVE_OUTPUT_FILENAME,TPYE,RATE)
	print VoiceRespone

	if VoiceRespone == "打开百度":
		url = 'http://www.baidu.com'
	else:
		print "我没听清"
		print "将打开苹果官网"
		url = "http://www.apple.com/cn/"
	webbrowser.open(url)
	print webbrowser.get()

if __name__ == '__main__':
	record()