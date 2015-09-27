# -*- coding: utf-8 -*-

import redis
import json
import uuid

"""
USERS
	users:%name:uid #string
        users:%name:safety #hash
        users:%name:info #hash
        users:%name:loginfo #hash
	users:%name:email #string
	users:%name:roles #list
        users:%uid:sid #string
        users:%sid:username #string
users:%name:info
        uid #string
        sid #string
        sex #string
        age #string
"""

"""
input : username
return: userinfo
"""
get_users_info_lua = """
local v_data = redis.call('HGETALL','users:' .. KEYS[1] .. ':info');
local result_set = {};
for idx = 1 ,#v_data,2 do
    result_set[v_data[idx]] = v_data[idx+1];
end
return cjson.encode(result_set);
"""
# uid #string
# sid #string
# sex #string
# age #string

set_users_info_lua = """
local user_info = cjson.decode(KEYS[2]);
for k, v in pairs(user_info) do
    redis.call('HSET','users:' .. KEYS[1] .. ':info',k,v);
end
return 1;
"""

# users:%name:safety
#         salt #string
#         passwd #string
#         authcode #string
get_users_safety_lua = """
local v_data = redis.call('HGETALL','users:' .. KEYS[1] .. ':safety');
local result_set = {};
for idx = 1 ,#v_data,2 do
    result_set[v_data[idx]] = v_data[idx+1];
end
return cjson.encode(result_set);
"""

set_users_safety_lua = """
local user_info = cjson.decode(KEYS[2]);
for k, v in pairs(user_info) do
    redis.call('HSET','users:' .. KEYS[1] .. ':safety',k,v);
end
return 1;
"""

class UserModel:
    class Users:
        safety = {} #hash #
""""
salt #string
passwd #string
authcode #string
"""
        info = {} #hash
        loginfo = {}#hash

	roles = [] #list
        sid = None #string
        uid = None #string
        username = None#string
        email = None #string
        sex = None #string
        age = None#string
        status = -1

    def __init__(self,db=None,pool=None):
        self.db = db if db else redis.Redis(pool)
        self._UserSha = {}
        self._init_users_sha()
        self._users = UserModel.Users
        pass
    def _init_users_sha(self):
        self._UserSha["get_user_info"] = self.db.execute_command("SCRIPT","LOAD",get_users_info_lua,parse="LOAD")
        self._UserSha["set_user_info"] = self.db.execute_command("SCRIPT","LOAD",set_users_info_lua,parse="LOAD")
        self._UserSha["get_user_safety"] = self.db.execute_command("SCRIPT","LOAD",get_users_safety_lua,parse="LOAD")
        self._UserSha["set_user_safety"] = self.db.execute_command("SCRIPT","LOAD",set_users_safety_lua,parse="LOAD")
        pass
    def setUserBase(self,username,email):
        rc = self.db.sismember("sys:username:list",username)
        if rc == 0:
            self.db.sadd("sys:users:namelist",username)
            self._users.uid = self.db.incr("sys:users:lastuid")
            self._users.username = username
            self._users.safety["salt"]= uuid.uuid4().hex
            self._users.status = -1 # not set passwd
            pass
        else:
            return -1
        pass
    def getUserBase(self,username):
        pass
    def checkUserName(self,username):
        pass
    def getUserInfo(self,username):
        user_info = {}
        user_info = self.db.execute_command("EVALSHA",self._UserSha["get_user_info"],1,username)
        return user_info if user_info else None

    def setUserInfo(self,username,userinfo):
        retmsg = self.db.execute_command("EVALSHA",self._UserSha["set_user_info"],2,username,r'%s'%(json.dumps(userinfo)))
        pass

    def getUserSafety(self,username):
        user_safety = {}
        user_safety = self.db.execute_command("EVALSHA",self._UserSha["get_user_safety"],1,username)
        return user_safety if user_safety else None

    def setUserSafety(self,username,usersafety):
        retmsg = self.db.execute_command("EVALSHA",self._UserSha["set_user_safety"],2,username,r'%s'%(json.dumps(usersafety)))
        pass


if __name__ == "__main__":
    r = redis.Redis(host="localhosst",port=6379,db=0)
