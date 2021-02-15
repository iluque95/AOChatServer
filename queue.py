# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.inputQueue = []
            
    def enqueueInput(self, msg):
        self.inputQueue.append(msg)
        
    def dequeueInput(self):
        try:
            return self.inputQueue.pop(0)
        except:
            raise ValueError("Input Queue is empty")
