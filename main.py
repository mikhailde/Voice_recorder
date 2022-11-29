import eel

eel.init('web', allowed_extensions=['.js', '.html'])

@eel.expose                     
def say_hello_py(x):
    print('Hello from %s' % x) 

eel.start('hello.html')