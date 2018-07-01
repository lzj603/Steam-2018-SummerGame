#!/bin/python3
# -*- coding: UTF-8 -*-
##Refer to sffxzzp's "account.py" and edited for multi accounts input
##Thank to sffxzzp's contributions for stcn!Therefor,this is just for self-use.
import os, re, sys, json

class filelib:
        def write(self, path, content, mode='w', encoding="gbk"):
                file = open(path, mode, encoding=encoding)
                file.write(content)
                file.close()
                return True
        def mkdir(self, dirname):
                try:
                        os.mkdir(dirname)
                except:
                        pass
                return True

def myinput(data):
        try:
                return input(data[0])
        except:
                return input(data[1])

def myprint(data):
        try:
                print(data[0])
        except:
                print(data[1])

def myloop(name, token, steamid):
        while name == "":
                name = myinput(['请输入Bot名：', 'Please input bot name:'])
        myprint(["访问 https://steamcommunity.com/saliengame/gettoken 以获取token。", "Open https://steamcommunity.com/saliengame/gettoken to get token."])
        while token == "":
                token = myinput(['请输入token：', 'Please input token:'])
        myprint(["访问 https://steamcommunity.com/my/?xml=1 以获取Steam 64位ID：", "Open https://steamcommunity.com/my/?xml=1 to get your steam 64 id."])
        while steamid == "":
                steamid = myinput(["请输入Steam 64位ID：", "Please input Steam 64 ID:"])
        filelib().write('configs/'+name+'.json', json.dumps({"token": token, "steamid": steamid}))

def myinputyn(flag):
        if (flag == "y") | (flag == "n"):
                return True
        else:
                return False

def main():
        flag = ''
        filelib().mkdir('configs') 
        while True:
                name = ''
                token = ''
                steamid = ''
                myloop(name, token, steamid)
                flag = myinput(['是否输入新账号【y/n】：', 'Input another account[y/n]:'])
                while(not myinputyn(flag)):
                        flag = myinput(['是否输入新账号【y/n】：', 'Input another account[y/n]:'])
                if flag == "n":
                        myprint(['用户选择n，即将退出', 'User choose \'n\' to exit'])
                        break

if __name__ == '__main__':
        main()
