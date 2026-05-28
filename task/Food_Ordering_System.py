from abc import abstractmethod,ABC
import random

class FoodOrder(ABC):
    def __init__(self):
        self.__price = 0
        
    @abstractmethod
    def order(self,item, price):
        pass
    
    @abstractmethod
    def cancel_order(self,item):
        pass
    @abstractmethod
    def get_order_id(self):
        pass
    
    def bill(self,price):
        print('======BILL========')
        print(f'Order ID: {self.get_order_id()}')
        print(f'total Price  : {price}')
        print('======BILL========')

class OrderHistry(FoodOrder):
    history = []
    
    @classmethod
    def add_history(cls,platform,order_id , item,price, status):
        cls.history.append({
            "platform":platform,
            "order id":order_id,
            "item":item,
            "price":price,
            "status":status
        })
    @classmethod
    def show_history(self):
        print("=======History======")
        for recorde in self.history:
            print(recorde)
            

class Foodmandu(FoodOrder):
    def __init__(self):
        super().__init__()
        self.__order_id= f'FDM-{random.randint(1000,9999)}'
    
    def order(self, item, price):
       assert price>0 ,"Price must be positive"
       
       self.__price = price
       print(f'Foodmandu order succesful , {item} Rs {price}')
       
       OrderHistry.add_history(
           "foodmandu",self.__order_id,item,price,"Ordered"
       )
        
    def cancel_order(self, item):
        print(f'Foodmandu order {item} is canceled ')
        
        OrderHistry.add_history("Foodmandu",self.__order_id,item,self.__price,"Canclled")
             
    def get_order_id(self):
        return self.__order_id
    
class PathaoFood(FoodOrder):
    def __init__(self):
        super().__init__()
        self.__order_id = f'PTF-{random.randint(1000,9999)}'
        
    def order(self, item, price):
        assert price>0 ,"price must be positive"
        
        self.__price=price
        print(f"Pathoa Order Successful : {item} Rs {price}")
        
        OrderHistry.add_history("PathaoFood",self.__order_id,item,price,"Ordered")
        
    def cancel_order(self, item):
        print(f'Pathoa order {item} is canceled ')
        OrderHistry.add_history("Pathoa Order", self.__order_id,item,self.__price,"Cancelled")
    
    def get_order_id(self):
        return self.__order_id
f1 = Foodmandu()
p1 = PathaoFood()


# Polymorphism
orders = [f1, p1]

items = [("Pizza", 1200), ("Burger", 500)]

for app, data in zip(orders, items):

    item, price = data

    app.order(item, price)

    app.bill(price)


# Cancel one order
f1.cancel_order("Pizza")


# Show history
OrderHistry.show_history()