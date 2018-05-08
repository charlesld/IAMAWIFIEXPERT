#coding:utf-8
#!/usr/bin/env python
#Created by Charles on 2018/3/1


import tokenlib
import tokenize

print (tokenlib.make_token({"user":12},))


def ssx(**kwargs):
    print(kwargs["ss"])



ssx(**{"ss":21})