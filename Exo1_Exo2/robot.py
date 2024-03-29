import time
class Robot():
    __name = "<unnamed>"
    __power = 'running'
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    __battery_full = False 

    def __init__(self, name ):
      self.set_name = name
    @property
    def put_on(self):
      self.__power = 'running'
    @property
    def put_off(self):
      self.__power = 'shutown'
    @property
    def state(self):
      return self.__power
    def recharge(self) :
        start = time.time()
        while not(self.__battery_full) :
          actuelle = time.time()
          if actuelle-start > 1 :
            time_delay = actuelle-start 
            self.__battery_level += round(time_delay *10,0)
            start = time.time()
            print(str(self.battery)+"%")
          if self.battery >= 100 :
            self.__battery_level = 100
            self.__battery_full = True

        else :
           return 
        
    @property
    def battery(self):
       return self.__battery_level 
    
    @property 
    def name(self) :
      return self.__name 
    @name.setter
    def set_name(self,name) :
      self.__name = name

    @property
    def speed(self) :
       return self.__current_speed
    
    @speed.setter
    def set_speed(self,speed) :
      str_speed =str(speed)
      if str_speed[0] == '-' : 
        if str_speed[1:].isdigit():     
          if speed >=-10 and speed <=20 : 
            self.__current_speed = speed
        else : 
          print("Entrer un nombre")
      else :
        if str_speed.isdigit() : 
          if speed >=-10 and speed <=20 : 
            self.__current_speed = speed
        else : 
          print("Entrer un nombre")

  
     
    @property
    def stop(self):
      self.set_speed = 0

    def status(self) :
        print("Hy, i am "+ str(self.name) )
        print("Etat "+ str(self.state) )
        print("Battery : " + str(self.battery))
        print( "speed :"+ str(self.speed))
    """
      Give your best code here ( •̀ ω •́ )✧
    """



############################

#print("The time used to execute this is given below")

#end = time.time()

##print(end - start)
