import eel
import wx
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
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK: path = dialog.GetPath()
    else: path = None
    dialog.Destroy()
    os.system(f'cp {path} web/backend/files')

eel.start('login/login.html')
