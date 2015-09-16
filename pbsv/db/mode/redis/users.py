# -*- coding: utf-8 -*-

import redis
class UserMode:
    def __init__(self,db=None,pool=None):
        self.db = db if db else redis.Redis(pool)
        pass

    def getUserInfo(self,username):
        user_info = {}
        user_info["uid"] = self.db.get("users:%s:uid"%(username))
        user_info["info"] = self.db.smembers("users:%s:info"%(username))
        return user_info if user_info else None

    def getUserSecurity(self,username):
        user_security = {}
        user_security["uid"] = self.db.get("users:%s:uid"%(username))
        user_security["security"] = self.db.smembers("users:%s:security"%(username))
        return user_security if user_security else None


if __name__ == "__main__":
    r = redis.Redis(host="localhosst",port=6379,db=0)
