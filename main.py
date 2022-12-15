import eel
import web.backend.record as record
import threading
import os
user_name = ''


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

@eel.expose
def username(name):
    global user_name
    user_name = name
    print(name)

@eel.expose
def printing():
    print(123)

eel.start('login/login.html')
