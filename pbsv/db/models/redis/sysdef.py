# -*- coding: utf-8 -*-

#sys:username:list #hash

class SysDef:
    def __init__(self,db=None,pool=None):
            def __init__(self,db=None,pool=None):
        self.db = db if db else redis.Redis(pool)
        self._SHA = {}
        self._init_sha()
        pass
    def usersname(self):
        self.db.sadd("sys:username:list","test")
    def _init_sha(self):
        pass
#        self._SHA["get_user_info"] = self.db.execute_command("SCRIPT","LOAD",get_users_info_lua,parse="LOAD")


