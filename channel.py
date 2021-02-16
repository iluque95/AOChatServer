from typing import List
from channelInterface import *
from user import *
from collections import deque
from channels import *

class Channel(ChannelInterface):

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


        print("Subject: Notifying observers...")

        while self.queue:
            msg = self.queue.popleft()
            
            for observer in self._observers:
                observer.update(self, msg, idChannel)

    def addPacket(self, data) -> None:

        self.queue.append(data)

        