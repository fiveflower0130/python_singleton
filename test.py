class FoodLogger():
    def __init__(self):
        self.foodLog = []
        
    def log(self, order):
        self.foodLog.append(order)
        
class FoodLoggerSingleton():
    _instance = None
      
    def __init__(self):
        if FoodLoggerSingleton._instance is not None:
            raise Exception('instance is exist')
        else:
            FoodLoggerSingleton._instance = FoodLogger()
            
    @staticmethod
    def get_instance():
        if FoodLoggerSingleton._instance is None:
            FoodLoggerSingleton()
        return FoodLoggerSingleton._instance
    
    
    
foodLooger = FoodLoggerSingleton().get_instance()

class Customer:
    def __init__(self, info):
        self.name = info['name']
        self.age = info['age']
        self.gender = info['gender']
        self.height = info['height']
        self.weight = info['weight']
        self.order = info['order']
        foodLooger.log(info)
        
class Restaurant:
    def __init__(self, order):
        self.no = order['no']
        self.price = order['price']
        self.order_food = order['order_food']
        self.remarks = order['remarks']
        foodLooger.log(order)

order_1 = {
    'no': '1',
    'price': 80,
    'order_food': ["beef hamburger", "coke"],
    'remarks':['no pickle', 'make beef larger']
}
order_2 = {
    'no': '2',
    'price': 50,
    'order_food': "french fries",
    'remarks':['make beef larger']
}
order_3 = {
    'no': '3',
    'price': 50,
    'order_food': "fried chicken",
    'remarks':['no pepper']
}
person_1 = {
    'name': 'Bill',
    'age': '26',
    'gender': 'male',
    'height': 175,
    'weight': 68,
    'order': order_1
}

person_2 = {
    'name': 'Mary',
    'age': '19',
    'gender': 'female',
    'height': 160,
    'weight': 45,
    'order': order_2
}

person_3 = {
    'name': 'Tom',
    'age': '35',
    'gender': 'male',
    'height': 168,
    'weight': 70,
    'order': order_3
}

cus_1 = Customer(person_1)
cus_2 = Customer(person_2)
cus_3 = Customer(person_3)
a_order = Restaurant(cus_1.order)
b_order = Restaurant(cus_2.order)
c_order = Restaurant(cus_3.order)
print(foodLooger.foodLog)
