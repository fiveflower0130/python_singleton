class SingleTon:
    _instance = None
    
    def get_instance():
        if SingleTon._instance is None:
            SingleTon()
        return SingleTon._instance
    
    def __init__(self):
        if SingleTon._instance is not None:
            raise Exception('instance is exist!')
        else:
            self._id = id(self)
            SingleTon._instance = self
    def get_id(self):
        return self._id