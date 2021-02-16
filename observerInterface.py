from __future__ import annotations
from abc import ABC, abstractmethod

class ObserverInterface(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, channelId, msg) -> None:
        """
        Receive update from subject.
        """
        pass