from abc import abstractmethod
from abc import ABCMeta

class FamilyAbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def getFamily(self):
        pass