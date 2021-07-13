# standard mode
class SingleTon1:
    _instance = None
    
    @staticmethod
    def get_instance():
        if SingleTon1._instance is None:
            SingleTon1()
        return SingleTon1._instance
    
    def __init__(self):
        if SingleTon1._instance is not None:
            raise Exception('instance is exist!')
        else:
            self._id = id(self)
            SingleTon1._instance = self
            
    def get_id(self):
        return self._id

# quick mode
class _SingleTon2:
    def __init__(self):
        self._id = id(self)
        self.log = []
        
    def get_id(self):
        self.log.append("1")
        return self._id, self.log

# metaclass mode
class SingletonMetaclass(type):
    #*args->未指定參數會以list形式傳回 **kwargs是指指定名稱參數以dict的方式傳回
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    
    #若使用class來建構物件時，以此來訂定物件的初始
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Singleton3(metaclass=SingletonMetaclass):
    def __init__(self):
        self._id = id(self)

    def get_id(self):
        return self._id
    
    
class SingleTonNew:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
p = _SingleTon2()   

# print("standard method: {}".format(SingleTon1.get_instance().get_id()))
# print("module method: {}".format(p.get_id()))
# print("metaclass method: {}".format(Singleton3().get_id()))
s1 = SingleTonNew(a=11, b=21)
s2 = SingleTonNew(a=11, b=21)
print(id(s1))
print(id(s2))