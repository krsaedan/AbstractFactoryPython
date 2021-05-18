from familyFactory.family1AbstractFactory import Family1AbstractFactory
from familyFactory.family2AbstractFactory import Family2AbstractFactory

class StackFamilyAbstractFactory():

    isFamily1: bool = False

    def getFamilyFactory(self):
        if(self.isFamily1):
            return Family1AbstractFactory()
        else:
            return Family2AbstractFactory()

