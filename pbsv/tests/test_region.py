#!/usr/bin/env python3
import pdb

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
    Type = "dbtype"
    def __init__(self,keyname):
        raise PBErrorKey("not found key name")

    @property
    def type(self):
        return self.__class__.Type

    def __str__(self):
        return self.Type


class PBTypeString(PBType):
    Type = "dbstring"
    def __init__(self,keyname):
        pass

class PBTypeHash(PBType):
    Type = "dbhash"
    def __init__(self,keyname):
        pass

class DBRegion(object):
    __space_name__ = "top"
    def __init__(self,zonename=None):
        if(zonename == None):
            self._zone_name = self.__class__.__space_name__
        else:
            self._zone_name = zonename
        pass

    @property
    def zone_name(self,zonename):
        self._zone_name = zonename

    def search(self,pb,keyname=None,function=None,data=None):
        if(pb.db == None):raise PBErrorDB("data base unconfigure")
        if(pb.type == PBTypeString.Type):
            return db.get(keyname)
        pass

    def init(self):
        pass

class TestTop1(DBRegion):
    __space_name__ = "sys"
    def init(self):
        pass

    def print_name(self):
        print  self._zone_name

if __name__ == "__main__":
    t1 = TestTop1()
    t1.print_name()
    pass
