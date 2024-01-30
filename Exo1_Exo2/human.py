from aliment import Aliments
class Human :
    __sex = 'non_binaire' 
    __energie = 50
    __stomac = []
    def __init__(self,sex,name='no name') :
        self.__sex=sex
        self.__name = name

    def eat(self,*args):
        for i in args : 
            print(str(self.__name) + " mange "+ str(i.name) +"  il trouve que c'est bon " ) 
            self.__stomac.append(i)
            if len(self.__stomac) > 5 :
                self.__vommir()

    def digest(self, ):
        
        for aliment in self.__stomac :
            
            if aliment._can_eat :
                self.__energie += aliment.nutriscore 
                if self.__energie > 100 :
                    self.__energie = 100
                print("l'aliment " + str(aliment.name) + " a été  digéré")
                
            else :
                self.__energie -= aliment.nutriscore 
                if self.__energie < 0 :
                    self.__energie = 0
                print("l'aliment " + str(aliment.name) + " n'a pas pu etre correctement digéré")
            print("l'energie de  " + str(self.__name) + "est de "+ str(self.energie))
        self.__stomac = []
    @property      
    def sexe(self):
        return self.__sex
    @property
    def energie(self):
        return self.__energie
    
    def __vommir(self):
        self.__energie -=35
        print(str(self.__name) + "est en train de vommir, il a trop mangé")
        print("l'energie de  " + str(self.__name) + "est de "+ str(self.energie))
        self.__stomac = []
if __name__=="__main__" :

    polo = Human(sex = "tractopelle",name = "francois")
    
    banana = Aliments("banana", 15 ,True) 
    Andy = Aliments("Andy", 40 , False) 
    pomme = Aliments("pomme", 30,True ) 
    carotte = Aliments("carotte", 10,True ) 

    polo.eat(banana,Andy,pomme,carotte)
