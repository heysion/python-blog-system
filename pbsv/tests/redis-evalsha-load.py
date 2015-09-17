# -*- coding: utf-8 -*-

import redis
import json
import pdb

test_lua = """
local value = redis.call('GET', KEYS[1])
value = tonumber(value)
return value * ARGV[1]
"""

test_table_lua = """
local value = redis.call('smembers', KEYS[1])
return value
"""

get_hash_lua = """
local keyvalues = redis.call('HGETALL', KEYS[1]);
local result = {};
for idx = 1, #keyvalues, 2 do
    result[keyvalues[idx]] = keyvalues[idx + 1]
end
return cjson.encode(result);
"""

if __name__ == "__main__":
    r = redis.StrictRedis(host='192.168.10.2', port=6379, db=8)
    r.set("foobar",10)
    multiply = r.register_script(test_lua)
    print multiply(keys=['foobar'], args=[5])
    print multiply.sha
    table_new = r.register_script(test_table_lua)
    retmsg = table_new(keys=["test"])
    print table_new.sha
    print retmsg
    print type(retmsg)
    table_new = r.register_script(get_hash_lua)
    retmsg = table_new(keys=["pt"])
    print table_new.sha
    print json.loads(retmsg)
    print type(retmsg)
    print r.hgetall("pt")
    pass
