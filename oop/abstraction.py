'''abstraction: the process of handling compexity by hidding unncessary data from user

abstraction class : blueprint of other class
abstraction class : a class that contain a least one abstract method
abstraction method: a method that has declaration but not any implementation
'''

from abc import abstractmethod ,ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def breaks(self):
        pass
    
    
class Bike(Vehicle):
    def show(slef):
        print(f'my bike is ready!!!!!!')
    
    def start(self):
        return super().start()
        
    def breaks(self):
        return super().breaks()

# ob =Bike()
# ob.show()
