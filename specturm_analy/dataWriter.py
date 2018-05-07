#coding:utf-8
#!/usr/bin/env python
#Created by Charles on 2018/4/28.

from influxdb import InfluxDBClient



class dataWriter():
    def __init__(self,ip):
        self.client = InfluxDBClient(ip, 8086, '', '', 'wifi',timeout=2)

    def write(self,data):
        self.client.write_points(data)


    def clean_data(self):
        self.client.drop_measurement("airdetect")

    def close_con(self):
        self.client.close()


if __name__ == '__main__':
    data = [
    {
        "measurement": "students",
        "tags": {
            "stuid": "s123",
            "sya":12
        },
        "fields": {
            "score": 89
        }
    }
]
    cc = dataWriter("172.16.0.115")
    cc.write(data=data)
