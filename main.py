class Animal_shelter:
    '''Class for monitoring animals in shelter'''
    
    def __init__(self):
        status_list = ['type','race','age','name','condition',"adoption_status"]
        self.animal_list = {'cats' : {},
                       'dogs' : {}}
    def add_animal(self):
        print('Please choose what kind of animal You want to add:')
        for i in self.animal_list:
            print(i)
        choice = input()
        try:
            choice.append()
        except:
            None


a = Animal_shelter()
a.add_animal()