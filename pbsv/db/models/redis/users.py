# -*- coding: utf-8 -*-

import redis
get_users_info_lua = """

"""
class UserModel:
    def __init__(self,db=None,pool=None):
        self.db = db if db else redis.Redis(pool)
        pass

    def getUserInfo(self,username):
        user_info = {}
        user_info["uid"] = self.db.get("users:%s:uid"%(username))
        user_info["info"] = self.db.smembers("users:%s:info"%(username))
        return user_info if user_info else None

    def setUserInfo(self,username,userinfo):
        user_info = {}
        pass

    def getUserSafety(self,username):
        user_safety = {}
        user_safety["uid"] = self.db.get("users:%s:uid"%(username))
        user_safety["safety"] = self.db.smembers("users:%s:safety"%(username))
        return user_safety if user_safety else None



if __name__ == "__main__":
    r = redis.Redis(host="localhosst",port=6379,db=0)
