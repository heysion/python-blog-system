# -*- coding: utf-8 -*-

import redis
import json

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

class UserModel:
    def __init__(self,db=None,pool=None):
        self.db = db if db else redis.Redis(pool)
        self._UserSha = {}
        self._init_user_info()
        pass
    def _init_user_info(self):
        self._UserSha["get_user_info"] = self.db.execute_command("SCRIPT","LOAD",get_users_info_lua,parse="LOAD")
        self._UserSha["set_user_info"] = self.db.execute_command("SCRIPT","LOAD",set_users_info_lua,parse="LOAD")
        pass

    def getUserInfo(self,username):
        user_info = {}
        user_info = self.db.execute_command("EVALSHA",self._UserSha["get_user_info"],1,username)
        # user_info["uid"] = self.db.get("users:%s:uid"%(username))
        # user_info["info"] = self.db.smembers("users:%s:info"%(username))
        return user_info if user_info else None

    def setUserInfo(self,username,userinfo):
        retmsg = self.db.execute_command("EVALSHA",self._UserSha["set_user_info"],2,username,r'%s'%(json.dumps(userinfo)))
        pass

    def getUserSafety(self,username):
        user_safety = {}
        user_safety["uid"] = self.db.get("users:%s:uid"%(username))
        user_safety["safety"] = self.db.smembers("users:%s:safety"%(username))
        return user_safety if user_safety else None


if __name__ == "__main__":
    r = redis.Redis(host="localhosst",port=6379,db=0)
