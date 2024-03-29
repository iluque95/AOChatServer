from typing import List
from collections import deque
from .observable import *
from .user import *
from .channels import *

class Channel(Observable):

    _observers: List = []

    queue = deque()

    def __init__(self, id):
        self.channelId = id

    def attach(self, observer):
        tsPrint(observer.name + ": Attached to channel " + Channels(self.channelId).name + ".")
        self._observers.append(observer)

        return self

    def detach(self, observer) -> None:
        self._observers.remove(observer)


    def notify(self) -> None:

        while self.queue:
            msg = self.queue.popleft()

            if msg:

                tsPrint("["+Channels(self.channelId).name+"] Notifying observers...")
            
                for observer in self._observers:
                    observer.update(self.channelId, msg)

    def addPacket(self, data) -> None:

        self.queue.append(data)

        