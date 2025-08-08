import pyaudio
import soundfile as sf
import sounddevice as sd
from pathlib import Path
import threading 
import time


class AudioPlayback:

    def __init__(self, controler):
        #player states
        self.playing = False
        self.pause = True
        self.stop_stream = False 


        self.controler = controler
        self.TrackPath = None
        self.p = None
        self.stream = None
    
    def startAudioStream(self):
        if not self.playing and self.controler.TrackPathArray is not None:
            self.playing = True
            self.stop_stream = False
            self.stream_thread =threading.Thread(target=self.playbackAudio)
            self.stream_thread.daemon = True 
            self.stream_thread.start()

    def pauseAudioStream(self):
        if self.playing:
            self.pause = not self.pause
            #update in view that its paused
    
    def killAudioStream(self):

        if self.playing:
            self.stop_stream = True


    def playbackAudio(self):
        for track_path in self.controler.audio_files:
            #unnecesary
            try:
                with sf.SoundFile(track_path, 'r') as file:
                    samplerate = file.samplerate
                    channels = file.channels

                    chunk = 1024

                    self.p = pyaudio.PyAudio()

                    self.stream = self.p.open(
                        format=pyaudio.paFloat32,
                        channels=channels,
                        rate=samplerate,
                        output=True)

                    data = file.read(chunk, dtype='float32')

                    while(len(data)>0) and not self.stop_stream:

                        if self.pause is not False:
                            self.stream.write(data.tobytes())
                            data = file.read(chunk, dtype='float32')
                        else:
                            time.sleep(0.1)

            except Exception as ex:
                print(f'Error whilst playback: {ex}')

            finally:
                if self.stream: self.stream.close()
                if self.p: self.p.terminate()
                self.is_playing = False
                self.is_paused = False


if __name__=='__main__':
    print('sybau')

