from abstractFactory.familyAbstractFactory import FamilyAbstractFactory
from family.family2 import Family2

class Family2AbstractFactory(FamilyAbstractFactory):
    def getFamily(self):
        return Family2()