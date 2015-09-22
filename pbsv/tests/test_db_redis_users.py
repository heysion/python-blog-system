# -*- coding: utf-8 -*-

import redis
import json
import os
import unittest
import sys

import pdb


get_users_info_lua = """
local v_data = redis.call('HGETALL','users:' .. KEYS[1] .. ':info');
local result_set = {};
for idx = 1 ,#v_data,2 do
    result_set[v_data[idx]] = v_data[idx+1];
end
return cjson.encode(result_set);
"""

try:
    import pbsv
except :
    sys.path.append("../../")
    try:
        import pbsv.tests
    except:
        raise

from pbsv.db.models.redis.users import UserModel

class TestdbRedisUsers(unittest.TestCase):
    def setUp(self):
        r = redis.Redis(host="192.168.10.2",port=6379,db=8)
        self.users = UserModel(db=r)
    def test_set_user_info(self):
        self.users.setUserInfo("test",userinfo={"age":10,"sid":"1002","uid":"a111","sex":1})

if __name__ == "__main__":
    unittest.main()
    os.exit()
    # cmd = r'redis-cli -n 8 -h 192.168.10.2 SCRIPT LOAD "%s" ' %(get_users_info_lua)
    # print(cmd)
    # os.system(cmd)
    r = redis.StrictRedis(host='192.168.10.2', port=6379, db=8)
    sha = r.execute_command(
        "SCRIPT", "LOAD", get_users_info_lua, parse="LOAD")
    print(sha)
    retmsg = r.execute_command(
        "EVALSHA" , sha ,1,"test")
    print(retmsg)
#    multiply = r.register_script(test_lua)
#   print multiply(keys=['foobar'], args=[5])
    pass
