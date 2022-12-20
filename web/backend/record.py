import pyaudio
import wave
import os
username = 'goldy'


class Recorder():
    def __init__(self) -> None:
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = 3
        self.filename = f"{username}.wav"
        self.control = "web/backend/files/control"

    def record(self):
        if os.path.isfile(self.control):
            with open(self.control, 'w') as f:
                f.write("stop")
        else:
            p = pyaudio.PyAudio()  # Create an interface to PortAudio
            print('Recording')
            stream = p.open(format=self.sample_format,
                            channels=self.channels,
                            rate=self.fs,
                            frames_per_buffer=self.chunk,
                            input=True)
            frames = []  # Initialize array to store frames
            flag = True
            os.system(f'echo "start" > {self.control}')
            while flag:
                # Store data in chunks
                data = stream.read(self.chunk)
                frames.append(data)
                with open(self.control, 'r') as f:
                    if 'stop' in f.readline():
                        flag = False
            # Stop and close the stream
            stream.stop_stream()
            stream.close()
            # Terminate the PortAudio interface
            p.terminate()
            print('Finished recording')
            # Save the recorded data as a WAV file
            os.chdir('web/backend/files/')
            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(frames))
            wf.close()
            os.chdir('../../../')
            os.unlink(self.control)


    def play(self):
        os.chdir('web/backend/files/')
        try:
            wf = wave.open(self.filename, 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=self.sample_format,
                            channels=self.channels,
                            rate=self.fs,
                            output=True)
            data = wf.readframes(self.chunk)
            while data != b'':
                stream.write(data)
                data = wf.readframes(self.chunk)
            stream.close()
            p.terminate()
        except: pass
        os.chdir('../../../')

        


def recording():
    global username
    with open('web/backend/files/username','r') as f: username = f.readline()
    rec = Recorder()
    rec.record()

def listening():
    listen = Recorder()
    listen.play()


if __name__ == '__main__':
    recording()
