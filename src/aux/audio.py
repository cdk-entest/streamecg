import pyaudio
import numpy as np

class AudioRecorder():
    """
    Create an audio recorder
    """
    def __init__(self,chunkSize=4096,samplingRate=8000,channel=1):
        self.channel = channel
        self.format = pyaudio.paInt16
        self.chunkSize = chunkSize
        self.samplingRate = samplingRate
        self.p = pyaudio.PyAudio()
        self.stream_start()

    def stream_start(self):
        self.stream = self.p.open(format=self.format,channels=self.channel,\
                                  rate=self.samplingRate, input=True,\
                                  frames_per_buffer=self.chunkSize)

    def stream_stop(self):
        self.stream.stop_stream()
        self.stream.close()

    def close(self):
        self.stream_stop()
        self.p.terminate()

    def record(self):
        data = self.stream.read(self.chunkSize,exception_on_overflow=False)
        data = np.frombuffer(data,dtype=np.int16)
        return data

