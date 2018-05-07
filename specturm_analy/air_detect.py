# coding:utf-8
# !/usr/bin/env python
# Created by Charles on 2018/3/30.

"""
空口利用率，running on 树莓派

"""
import json

import datetime
import telnetlib
import time

from specturm_analy.dataWriter import dataWriter


class telData(object):
    def __init__(self, place, channel, band, db_ip):
        self.place = place
        self.channel = channel
        self.band = band
        self.writer = dataWriter(db_ip)

    def clean_data(self):
        self.writer.clean_data()
        self.writer.close_con()

    def do_telnet(self, Host, Port, username, password, confparase, pre_cmd, command, end_cmd,channel_ajd):
        tn = telnetlib.Telnet(Host, Port, timeout=1)
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b'\n')
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b'\n')
        tn.read_until(b"mode: ")
        tn.write(confparase.encode('ascii') + b'\n')
        tn.read_until(b'~ # ')
        tn.write(pre_cmd.encode('ascii') + b'\n')
        tn.write(channel_ajd.encode('ascii') + b'\n')
        tn.write(command.encode('ascii') + b'\n')
        time.sleep(.1)
        _ = (tn.read_very_eager())
        print("start")

        indexdic = []
        countn = 0
        while (countn < 1000):
            time.sleep(1)
            cc = tn.read_very_eager()
            cc = cc.decode()
            cc = cc.split()
            if cc and int(cc[1]) != 0:
                print(len(cc))
                if len(cc) != 11:
                    continue
                flag = True
                for c in cc:
                    try:
                        if int(c) < 0:
                            flag = False
                            print(cc)
                            break
                    except:
                        break

                if flag:
                    self.save_data(cc)

            countn += 1
        print('over')

        tn.write(end_cmd.encode('ascii') + b'\n')
        tn.close()
        self.writer.close_con()
        return indexdic

    def GetChannel(self):
        pass

    def save_data(self, data):
        model = [{
            "measurement": "airdetect",
            "tags": {
                "location": self.place,
                "channel": self.channel,
                "band": self.band,
            },
            "fields": {
                "CCA_PER": data[1],
                "EXT_CCA_PER": data[2],
                "RX_PER": data[3],
                "TX_PER": data[4],
                "OTHER_PER": data[5],
                "FREE_PER": data[6],
                "EXT_FREE_PER": data[7],
                "OFDMERR": data[8],
                "CCKERR": data[9],
                "TOTALERR": data[10]
            }
        }]
        self.writer.write(model)

def worker(band,channel,place):
    Host = '172.16.5.99'
    Port = '23'
    username = 'xx'
    password = 'xx'
    confparase = 'xx'
    login_fail = 'Login incorrect'
    conf_fail = 'Wrong password, please try again: '
    per_command = "ixx  "
    end_command = "xx"
    if band == 2.4:
        radio = "ap0_0"
    elif band == 5:
        radio = "ap1_0"
    channel_adj = "wlanconfig %s channel %s"%(radio,channel)
    command = 'xx'
    print(time.asctime(), ":   ****** begin", "\n")
    telData(place,channel, band, "172.16.0.115").do_telnet(Host, Port, username, password, confparase,
                                                                   per_command, command,
                                                                   end_command,channel_adj)

def clean():
    telData("2-1", 1, 2.4, "172.16.0.115").clean_data()


if __name__ == '__main__':
    # clean()
    worker(2.4,1,"3F-1g")
