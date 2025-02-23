from abc import ABC, abstractmethod

class Feedable(ABC):

    @abstractmethod
    def to_feed(self):
        pass

