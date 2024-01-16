from robot import Robot
from human import Human
from aliment import Aliments
class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe,name)

    def status(self):
        Robot.status(self)
        print("Energie :" + str(self.energie))


banana = Aliments("banana", 15 ,True) 
Andy = Aliments("Andy", 40 , False) 
pomme = Aliments("pomme", 30,True ) 
carotte = Aliments("carotte", 10,True ) 

cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')

#cyborg.recharge()
cyborg.status()
cyborg.eat(banana)
cyborg.eat(banana)
cyborg.eat(banana)
cyborg.eat(Andy,pomme,carotte)
cyborg.digest()


