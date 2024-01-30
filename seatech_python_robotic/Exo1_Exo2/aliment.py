class Aliments :
    def __init__(self,name, nutriscore,can_eat) :
        self.__name = name
        self.__nutriscore = nutriscore
        self._can_eat=can_eat
    @property
    def nutriscore(self):
        return self.__nutriscore
    
    @property
    def name(self):
        return self.__name
    
    @property
    def commestible_pour_human(self):
        return self._can_eat