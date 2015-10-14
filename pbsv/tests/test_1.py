#!/usr/bin/env python3

class PBError(object):
    def __init__(self,str):
        self.__error_str = str
    def __str__(self):
        return self.__error_str

class PBErrorKey(PBError):
    pass

class PBErrorDB(PBError):
    pass

class PBType(object):
    _type = "dbtype"
    def __init__(self,keyname):
        raise PBErrorKey("not found key name")

    @property
    def type(self):
        return self._type

class PBTypeString(PBType):
    _type = "dbstring"
    def __init__(self,keyname):
        pass
    def __str__(self):
        return self._type
    def __str__():
        return PBTypeString._type

class PBTypeHash(PBType):
    _type = "dbhash"
    def __init__(self,keyname):
        pass

class DBRegion(object):
    __name__ = "top"
    def __init__(self,zonename):
        if(zonename == None):
            zonename == __name__
        self._zone_name = zonename
        pass

    def search(self,pb,keyname=None,function=None,data=None):
        if(pb.db == None):raise PBErrorDB("data base unconfigure")
        if(pb.type == PBTypeString.type):
            return db.get(keyname)
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
    t2 = PBTypeString("abc")
    print(t2.type)
    t3 = PBTypeHash("ab")
    print(t3.type)
    print(PBTypeHash.type)

