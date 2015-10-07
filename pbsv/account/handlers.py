# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pdb
import json

class HandlerBase(tornado.web.RequestHandler):
    def initialize(self):
        self.no_error = False
        self.req_json = {}

    def http_buffer_to_json(self):
        print self.request.body
        if len(self.request.body):
            try:
                self.no_error = True
                self.req_json = json.loads(self.request.body)
            except ValueError, e:
                self.no_error = False
                print e
            except KeyError, e:
                self.no_error = False
                print e
            except AttributeError, e:
                self.no_error = False
                print e
            finally:
                pass

class MainLoginHandler(HandlerBase):
    def get(self):
        pass
    def post(self):
        pass

class LoginHandler(HandlerBase):
    def get(self):
        pass
    def post(self):
        self.http_buffer_to_json()
        username = self.req_json.get('username')
        password = self.req_json.get('password')
        if not username or not password:
            data = {'retcode': 404, 'retmsg': 'Missing parameters!'}
            data_json = json.dumps(data)
            self.write(data_json)
            return self.redirect('/user/login')
        else:
            users_models = UserModels(username,password)
            result = users_models.login()
            result = 0
            if result:
                self.set_secure_cookie("user", users_models._username)
                data = {'retcode': 200, 'retmsg': 'Logout successed!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/')
            else:
                data = {'retcode': 404, 'retmsg': 'Logout error!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/user/logout')
        pass

class LogoutHandler(HandlerBase):
    def get(self):
        self.http_buffer_to_json()
        username = self.req_json.get('username')
        password = self.req_json.get('password')
        if not username or not password:
            data = {'retcode': 404, 'retmsg': 'Missing parameters!'}
            data_json = json.dumps(data)
            self.write(data_json)
            return self.redirect('/user/login')
        else:
            users_models = UserModels(username,password)
            result = users_models.logout()
            result = 0
            if result:
                self.set_secure_cookie("user", users_models._username)
                data = {'retcode': 200, 'retmsg': 'Register successed!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/user')
            else:
                data = {'retcode': 404, 'retmsg': 'Create new account error!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/user/login')
        pass
    def post(self):
        pass


class RegisterHandler(HandlerBase):
    def get(self):
        pass

    def post(self):
        self.http_buffer_to_json()
        username = self.req_json.get('username')
        password = self.req_json.get('password')
        if not username or not password:
            data = {'retcode': 404, 'retmsg': 'Missing parameters!'}
            data_json = json.dumps(data)
            self.write(data_json)
            return self.redirect('/user/register')
        else:
            users_models = UserModels(username,password)
            result = users_models.create()
            result = 0
            if result:
                self.set_secure_cookie("user", users_models._username)
                data = {'retcode': 200, 'retmsg': 'Register successed!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/user')
            else:
                data = {'retcode': 404, 'retmsg': 'Create new account error!'}
                data_json = json.dumps(data)
                self.write(data_json)
                return self.redirect('/user/register')
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
