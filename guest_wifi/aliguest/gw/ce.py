#coding:utf-8
#!/usr/bin/env python
#Created by Charles on 2018/2/12.
import json

import cherrypy
import os
import tokenlib
tok = {"test":12345}

class StringGenerator(object):

    @cherrypy.expose
    def ping(self,**kwargs):
        return "Pong\nconf_ver=1\ncmd_ver=2"

    @cherrypy.expose
    def auth(self,**kwargs):
        print(kwargs)
        if kwargs.get("stage"):
            if kwargs["stage"] == "login":
                print("auth tol %s"%tok)
                print("kwargs.get(’token‘) %s "%kwargs.get("token"))

                if kwargs.get("token") in tok.values():
                    print("auth jhhhhh")
                    return "Auth: 1\n0 0 0 0 60 60"
        try:
            if int(kwargs.get("free_auth")) is 1:
                print("auth -----------------")
                return "Auth: 1\n0 0 0 0 60 60"
        except:
            pass

    @cherrypy.expose
    def conf(self,**kwargs):
        return "TrustedWANHOSTList www.baidu.com,www.sina.com.cn,www.163.com\n" \
               "StadctEnable yes\n" \
               "StadctRSSI 10\n" \
               "StadctRptTime 10\n" \
               "WanFlowStatSwitch yes\n"


    @cherrypy.expose
    def login(self,**kwargs):
        if kwargs.get("action") == "pc":
            return open('pc_index.html', encoding="utf-8")
        elif kwargs.get("action") == "phone":
            return open('phone_index.html', encoding="utf-8")
        return open('index.html',encoding="utf-8")


    @cherrypy.expose
    def veryfi(self,username,password):
        if username=="123123" and password == "123123":
            token_ram = tokenlib.make_token({"user":username})[:10]
            # token太长，有时gw会截断，重新生成，导致认证失败
            tok[username] = token_ram
            raise cherrypy.HTTPRedirect("http://172.16.100.1:8060/wifidog/auth?token=%s"%token_ram,status=302)
        else:
            return "wrong user or passwd!"

    @cherrypy.expose
    def portal(self,**kwargs):
        raise cherrypy.HTTPRedirect("http://www.taobao.com")



if __name__ == '__main__':
    cherrypy.config.update({
                            'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080,})
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)