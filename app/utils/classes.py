class JSONObject(object):
    def __init__(self, _dict):
        self.keys = []
        if type(_dict) == dict:
            self.keys = list(_dict.keys())
            for k,v in _dict.items():
                try:
                    self.__setattr__(k,v)
                except Exception:
                    pass

    def has(self,key):
        return key in self.keys

    def get(self,key):
        if self.has(key):
            return self.__getattribute__(key)
        return None

    def isnull(self,key):
        if self.has(key):
            return not bool(self.__getattribute__(key))
        self.keys.append(key)
        self.__setattr__(key,None)
        return True

    def hasall(self,keys):
        for key in keys:
            if not self.has(key):
                return False
        return True