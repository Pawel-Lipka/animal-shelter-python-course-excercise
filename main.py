import random
import guess_game

class Animal_shelter:
    '''Class for monitoring animals in shelter'''
    
    def __init__(self):
        self.status_list = ['type','race','age','name','condition (0-worst, 4 - best)',"adoption_status_0_ready_1_not_ready"] # list of animal conditions. Can be updated
        
        self.animal_list = {'cats': {},
                       'dogs' : {}} # list of animals
        
    def add_animal(self): # let you add animal to program
        print('Please choose what kind of animal You want to add:')
        for i in self.animal_list: # print out the list of animals from main animal list
            print(i)
        choice = input() # choose what kind of animal want to add 
        try: # check is there this animal in list
            self.animal_list[choice].update({len(self.animal_list[choice]) + 1 : {} }) # create next ID in choosed category. auto skip if no such category
            
            for status in self.status_list:
                self.animal_list[choice][len(self.animal_list[choice])].update({status : input(status)}) # input status of animal from status list to current(last) ID
        except: # if there is no animal in list ask if you want to add new kind
            add_new_kind = input('there is no such animal in our list do you want to add new kind of animal? y/n')
            try:
                if add_new_kind == 'y':
                    self.animal_list.update({input("type new kind of animal") : {}})
            except:
                print('unknow error')
        
    '''def adoption_ready(self):
        for i in self.animal_list: # print out the list of animals from main animal list
            print(i)
        choice = input('what animals you want to check if there any ready for adaoption:')
        for key in self.animal_list[choice]:
            if  self.animal_list[choice][i]["adoption_status_0_ready_1_not_ready"] == 0:
                self.animal_list[choice][i].remove
                print(self.animal_list)''' #remove all adoption ready animals from selected category
    
    def adoption_ready(self,animal_index): # wersja z zadania
        for animal_kind in self.animal_list:
            try:
                print(self.animal_list[animal_kind][animal_index])
                if self.animal_list[animal_kind][animal_index]["adoption_status_0_ready_1_not_ready"] == 0:
                    self.animal_list[animal_kind][animal_index].remove()
            except:
                break
        
    def present(self,animal):
        for i in self.animal_list[animal]:
            print(f'\n number: {i} in {animal}')
            for y in self.status_list:
                print(f'{y}: {self.animal_list[animal][i][y]}')
                  
                  
        
                
        
        
        
"""print('welcome to Animal Shelter')
shelter = Animal_shelter()
for i in range(2):
    shelter.add_animal()
shelter.present('cats')"""

guess_game. Game().guess()
