from abc import abstractmethod
from abc import ABCMeta

class Family(metaclass=ABCMeta):
    @abstractmethod
    def getFather(self):
        pass
    @abstractmethod
    def getSon(self):
        pass