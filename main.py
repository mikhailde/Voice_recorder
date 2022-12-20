import eel
import wx
import web.backend.record as record
import web.backend.csv_parser as csv_parser
import threading
import os
user_name = ''
path = ''


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
    with open('web/backend/files/username','w+') as f: f.write(user_name)
    print(name)

@eel.expose
def upload_file(wildcard="*"):
    global path
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK: path = dialog.GetPath()
    else: path = None
    dialog.Destroy()
    try:
        if path[path.find('.'):] == '.csv':
            os.system(f'cp {path} web/backend/files')
            path = 'web/backend/files/' + (path.split('/')[-1])
            return 'true'
    except: pass
    return 'false'

@eel.expose
def save_file(id):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.DD_DIR_MUST_EXIST
    dialog = wx.DirDialog(None, "Choose directory to save", style=style)
    if dialog.ShowModal() == wx.ID_OK: save_path = dialog.GetPath()
    else: return 'false'
    dialog.Destroy()
    try:
        os.system(f"mv web/backend/files/{user_name}.wav {save_path}/{user_name}_{id}.wav")
        return 'true'
    except: pass
    return 'false'


@eel.expose
def parser():
    print(csv_parser.parser(path))
    return csv_parser.parser(path)

@eel.expose
def listener(): record.listening()

@eel.expose
def write_log(log):
    os.system(f'echo "{", ".join(log)}" >> web/backend/files/logs.log')

eel.start('login/login.html')
