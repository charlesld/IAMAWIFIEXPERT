## wifi portal
听说你去过阿里巴巴，那你一定连过`Alibaba-guest`。  
想不想把`Alibaba-guest`带回家？给家里来做客的客人也用一用，顺带炫一下技术实力？（zhuangbility）  
now，教你用树莓派做一个’一毛一样‘的`Alibaba-guest`，这里为什么要引起来，因为穷，用不起验证码，改成密码了，就不是一毛一样了，有一点差别

#### 设备
1. AP一台
2. 树莓派一个
3. 环境 cherrypy

#### 过程 

1. AP ssid 设置成 `Alibaba-guest`

```angular2html
~ # iwconfig 
lo        no wireless extensions.

eth0      no wireless extensions.

eth1      no wireless extensions.

wifi0     no wireless extensions.

sit0      no wireless extensions.

br0       no wireless extensions.

ap0_0     IEEE 802.11ng  ESSID:"Alibaba-guest"  
          Mode:Master  Frequency:2.412 GHz  Access Point: 00:34:CB:A0:B5:4D   
          Bit Rate:130 Mb/s   Tx-Power=12 dBm   
          RTS thr=2346 B   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality=94/94  Signal level=-101 dBm  Noise level=-100 dBm
          Rx invalid nwid:7167  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0

``` 


2. AP 热点指向 树莓派，前提ap要能ping通树莓派。


```angular2html
device_hotspot_name=WIFI-A0B54D
device_hotspot_url=172.16.0.100:8080
device_hotspot_backupurl=
device_hotspot_path=/
```


3. 手机搜索Alibaba_guest ，点击连接，自动跳出认证页面，手机跳手机版，电脑跳电脑版

4. 这里是改成了手机号码与密码认证，如果有钱（一条要5分，哼哼），也可以接入短信验证码，更逼真。

5. 密码和手机号码都是预设的，方便省事，没读数据库和文件。

6. 认证成功后跳到www.taobao.com 是不是很逼真。。。。

7. 这样来客人了，不用分享家里wifi的密码，指导客人连接`Alibaba-guest`就可以上网了，当然要配置用户名和密码，只要修改一下代码就好，简单的可以使用文件，逼格高的就用mysql

8. last if you wanna own one AP , mail to me pppoe@139.com

> 做完效果怎么样  (这是电脑版，手机版后面做)
<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/aliguest_wifi_pc.jpg" width=500 height=250 />

[代码位置](guest_wifi/aliguest/gw/ce.py)


