
class PartyAnimal():
    x = 0
    def __init__(self, nam=''):
        self.name = nam
        print(f'{self.name} is constructed')

    def party(self):
        self.x = self.x + 1
        print(f'{self.name} party count',self.x)

    def __del__(self):
        print(f'{self.name} is destructed', self.x) 

'''an = PartyAnimal('animal');
an.party()
an.party()
an.party()
PartyAnimal.party(an)
an = 42 
print('an contains', an)
sara = PartyAnimal('Sara')
sara.party()
sara.party()
print(sara.name)'''