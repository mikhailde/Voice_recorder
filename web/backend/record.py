import pyaudio
import wave
import os


class Recorder():
    def __init__(self) -> None:
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = 3
        self.filename = "files/output.wav"
        self.control = "web/backend/control"

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
            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(frames))
            wf.close()
            os.unlink(self.control)


def recording():
    rec = Recorder()
    rec.record()


if __name__ == '__main__':
    recording()
