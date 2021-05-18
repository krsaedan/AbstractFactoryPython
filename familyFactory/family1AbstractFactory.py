from abstractFactory.familyAbstractFactory import FamilyAbstractFactory
from family.family1 import Family1

class Family1AbstractFactory(FamilyAbstractFactory):
    def getFamily(self):
        return Family1()