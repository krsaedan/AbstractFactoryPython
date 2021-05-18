from abstractFactory.stackFamilyAbstractFactory import StackFamilyAbstractFactory

stackFactory = StackFamilyAbstractFactory()
familyFactory = stackFactory.getFamilyFactory()
family = familyFactory.getFamily()
print(family.getFather())
print(family.getSon())
