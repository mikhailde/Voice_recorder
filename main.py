import eel
import web.backend.record as record
import threading


eel.init('web/frontend', allowed_extensions=['.js', '.html'])


class MyThread(threading.Thread):
    def run(self):
        record.recording()
        pass


@eel.expose
def say_hello_py(x):
    print('Hello from %s' % x)


@eel.expose
def recording():
    thread = MyThread()
    thread.daemon = True
    thread.start()


eel.start('hello.html')
