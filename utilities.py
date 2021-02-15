# -*- coding: utf-8 -*-

# import thread module 
from _thread import *
import threading
import socket
from collections import deque
import time
import datetime
print_lock = threading.Lock()

# CRAW; 09/02/2021 --> ThreadSafe
def tsPrint(msg):
    # lock acquired by client 
    print_lock.acquire()
    print(msg)
    # lock released on exit 
    print_lock.release() 

  