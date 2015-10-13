#!/usr/bin/env python3

class DBError(object):
    def __init__(self,str):
        self.__error_str = str
    def __str__(self):
        return self.__error_str

class DBKeyError(DBError):
    pass

class DBRegion(object):
    __name__ = "top"
    def __init__(self,zonename):
        if(zonename == None):
            zonename == __name__
        self._zone_name = zonename
        pass

class DBType(object):
    _type = "dbtype"
    def __init__(self,keyname):
        raise DBKeyError("not found key name")
    @property
    def type(self):
        return self.__class__._type

class DBTypeString(DBType):
    _type = "dbstring"
    def __init__(self,keyname):
        pass

class DBTypeHash(DBType):
    _type = "dbhash"
    def __init__(self,keyname):
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
    t2 = DBTypeString("abc")
    print(t2.type)
    t3 = DBTypeHash("ab")
    print(t3.type)

