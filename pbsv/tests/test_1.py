class DBKeyError:
    def __init__(self,str):
        self.__error_str = str
    def __str__(self):
        return self.__error_str
class DBRegion:
    __name__ = "top"
    def __init__(self,zonename):
        if(zonename == None):
            zonename == __name__
        self._zone_name = zonename
        # if(zonename == None) raise DBKeyError("not found zone name")
        pass


class Test:
    class t2:
        def __init__(self):
            print("t2")
    def __init__(self):
        print("test")
    def show(self):
        tt = Test.t2()

if __name__ == "__main__":
    t1 = Test()
    t1.show()
