import itertools
from guess_game import Game
class Zwierze:
    id_iter = itertools.count()
    def __init__(self,gatunek,rasa,wiek,imie,stan_zdrowia,status_adopcji):
        
        self.animal_id = next(Zwierze.id_iter) + 1
        self.gatunek = gatunek
        self.rasa = rasa
        self.wiek = wiek
        self.imie = imie
        self.stan_zdrowia = stan_zdrowia
        self.status_adopcji = status_adopcji
        
    def __repr__(self):
        
        if self.status_adopcji == 0:
            adopcja = 'przeznaczony do adopcji'
        else:
            adopcja = 'nie przeznaczony do adopcji'
        return f"{self.imie} - {self.rasa} - 'stan zdrowia: '{self.stan_zdrowia}/4 - {adopcja}"

class Schronisko:
    def __init__(self):
        self.koty = {}
        self.psy = {}
    
    def dodaj_zwierze(self,kot_lub_pies):
        
        if kot_lub_pies.gatunek == 'pies':
            self.psy[kot_lub_pies.animal_id] = kot_lub_pies
            
        elif kot_lub_pies.gatunek == 'kot':
            self.koty[kot_lub_pies.animal_id] = kot_lub_pies
        
        else:
            print('niema takiego zwierzecia')
            
    def po_adopcji(self, animal_id, gatunek):
        try:
            if gatunek == 'pies':
                imie = self.psy.get(animal_id).imie
                if self.psy.get(animal_id).status_adopcji == 0:
                    self.psy.pop(animal_id)
                    print(f'pies {imie} został adoptowany')
                else:
                    print(f'pies {imie} nie jest przeznaczony do adopcji')

            elif gatunek == 'kot':
                imie = self.koty.get(animal_id).imie
                if self.koty.get(animal_id).status_adopcji == 0:
                    self.koty.pop(animal_id)
                    print(f'kot {imie} został adoptowany')
                else:
                    print(f'kot {imie} nie jest przeznaczony do adopcji')
        
        except AttributeError:
            print("Prawdopodobnie jest zle ID")
        except:
            print('nieznany błąd')
            
    def lista_zwierzat(self, gatunek = 'wszystkie'):
        
        def komunikaty(gatunek):
            if gatunek == 'kot':
                info = 'KOTÓW'
                slownik = self.koty
            if gatunek == 'pies':
                info = 'PSÓW'
                slownik = self.psy
            
            print(10*'#')
            print(f'LISTA {info}')
            for klucz in slownik:
                print(klucz, '->', slownik[klucz])
            print(10*'#')
            
            
            
        if gatunek == 'wszystkie':
            komunikaty('pies')
            komunikaty('kot')
        elif gatunek == 'pies' or gatunek == 'psy':
            komunikaty('pies')
            
        elif gatunek == 'kot' or gatunek == 'koty':
            komunikaty('kot')
        
        else:
                print(f'niema takiego gatunku zwierząt jak {gatunek}')
    def gra(self):
        gra = Game()
        gra.guess()
'''testowe_zwierze = Zwierze('kot', '-', 43, 'Satan', 4, 0)
print(type(testowe_zwierze))
slownik_test = {'a' : 1 , 'b': 2}
testowe_zwierze1 = Zwierze('kot', 'domowy', 15, 'Kamil', 2, 1)
slownik_test[testowe_zwierze.animal_id] = testowe_zwierze
slownik_test[testowe_zwierze1.animal_id] = testowe_zwierze1
print(slownik_test)'''

schronisko1 = Schronisko()
kot1 = Zwierze('kot', 'dachowiec', 2, 'Sierżant', 4 , 1)
schronisko1.dodaj_zwierze(kot1)
schronisko1.lista_zwierzat('kot')
schronisko1.po_adopcji(1,'kot')
schronisko1.gra()