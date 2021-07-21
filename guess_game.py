import random
class Game:
    
    
    def drawing(self):
        return random.randint(0,100)
    
        
    def it_is_correct(self):
        try:
            while True:
                p_guess = int(input('Podaj liczbe'))
                if p_guess not in range(0,101):
                    print('liczba musi być między 0-100')
                else: return p_guess
        except: print('bląd')
        
    
    def guess(self):
        while True:
            draw = self.drawing()
            while True:
                p_guess = self.it_is_correct()
                if p_guess > draw:
                    print('podałeś za dużą liczbę')
                elif p_guess < draw:
                    print('podałeś za małą liczbę')
                else: 
                    print(f'gratuluje wygrałeś liczba wylosowana przez komputer to: {draw}')
                    break
            player_choose = input('Czy chcesz zagrać ponownie? y/n')
            if player_choose == 'n':
                print("exit")
                break
