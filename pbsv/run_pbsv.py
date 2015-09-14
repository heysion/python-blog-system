# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado
import tornado.httpserver
import tornado.web
import tornado.ioloop
import redis

from tornado.options import define ,options
from views import view as sub_handlers

define("port", default = 8080, help = "run on the given port", type = int)
define("db_host", default = "mysql_host", help = "community database host")
define("db_database", default = "db_name", help = "community database name")
define("db_user", default = "db_user", help = "community database user")
define("db_password", default = "db_password", help = "community database password")

class App(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug = True,
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        )
        handlers = [
#            (r"/",None),
        ]
        self._redis_pool =  redis.ConnectionPool(host="127.0.0.1", port=6379, db=1)
        handlers.extend(sub_handlers)
        tornado.web.Application.__init__(self,handlers,**settings)

def run_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run_server()

