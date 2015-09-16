# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pdb
import json

class BaseLoginHandler(tornado.web.RequestHandler):
    def get(self):
        print("abc")
        self.wirte("hello world!")
        self.finash()
        pass
    def post(self):
        pass

class MainLoginHandler(BaseLoginHandler):
    def get(self):
        pass
    def post(self):
        pass

class LoginHandler(BaseLoginHandler):
    def get(self):
        pass
    def post(self):
        pass

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        pass


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        pass

class PasswordHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        pass


handlers = [
    ('/user', MainLoginHandler),
    ('/user/login', LoginHandler),
    ('/user/logout', LogoutHandler),
    ('/user/register', RegisterHandler),
    ('/user/password', PasswordHandler),
]
