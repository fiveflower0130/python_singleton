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
    def __init__(self, order):
        self.name = order['name']
        self.price = order['price']
        self.food = order['food']
        foodLooger.log(order)


def main():
    c_order = {
        'name': 'c',
        'price': 60,
        'food': "brand"
    }
    d_order = {
        'name': 'd',
        'price': 200,
        'food': "beef"
    }
    c = Customer(c_order)
    d = Customer(d_order)
    print(foodLooger.foodLog)


if __name__ == "__main__":
    main()
