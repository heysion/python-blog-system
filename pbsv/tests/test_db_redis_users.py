# -*- coding: utf-8 -*-

import redis
import json
import pdb
import os

get_users_info_lua = """
local v_data = redis.call('HGETALL','users:' .. KEYS[1] .. ':info');
local result_set = {};
for idx = 1 ,#v_data,2 do
    result_set[v_data[idx]] = v_data[idx+1];
end
return cjson.encode(result_set);
"""

if __name__ == "__main__":
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
