# IAMAWIFIEXPERT
多年WIFI积累，留当变更行业后的一种回忆



## 先贴些酷酷的图


> 空口错误采集

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/channel%20err.jpg" width=500 height=250 />

> 站点勘测

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/site%20suvery.jpg" width=500 height=250 />


> 频谱空口利用率

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/specturm.jpg" width=500 height=250 />

> 无线环境抓取

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/wireless%20env.jpg" width=500 height=250 />




## 频谱分析
[air_detect](https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/specturm_analy/air_detect.py)
利用树莓派 与 AP  打造基于 grafana 与 influxdb 生成时序的 频点错误与空口利用率的状态



### 作用是什么？

wifi看不见摸不着，但是你得用。  
你是普通用户，只要能连上wifi，玩2把游戏就ok。。  
如果你是企业用户，几十个人在一个屋子里，大家都用wifi，干些频繁交互数据的工作，这时候，无线的好坏就是对大家的工作效率的直接影响因素了，当然，我是员工我可以不用管无线是否不好用，不好用正好可以偷个懒，甩个锅。
但是一个无线管理员，这就是他的责任范畴。致力于把好的无线带给每一个用户。不能给那些偷懒的家伙甩锅的借口。

那么怎么管理无线？
无线不比有线，你拿网线做个镜像开个wireshark 就能装装评估样子。  
无线以空气为介质，一般的抓包工具难对评估无线质量有很大帮助。（当然我自己的工具各种全，我想用什么用什么）  
所以简单的只能去做频谱分析，但是一般的频谱分析工具都很贵，非常贵，不是一般的贵。普通的管理员根本不会去买，甚至连想要拥有的勇气都没有。  
这里就是最大的重点了，利用白菜价的过时AP（不管无线调制技术如何先进，但始终基于这个频点发射接收），做一个带频谱分析的工具，真是太酷了。经济又高效。一下子就能洞穿无线的奥秘。

### 怎么用
树莓派1只
AP 1只

1. 刷入代码

2. 偷个懒，没写web管理，目前在树莓派使用命令行去获取数据

3. 使用时间序列作为管理模型，简单的绘出可视化数据，图里面的数据越小就越好。

4. 你可以尽情的调整无线的功率频点，直到出来的图数据越来越小。

5. 拿着工具，空余时间帮客户解决一些问题，赚点小钱。

### 效果


> 空口错误采集

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/channel%20err.jpg" width=500 height=250 />


> 频谱空口利用率

<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/specturm.jpg" width=500 height=250 />





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

8. last if you wanna buy a AP , mail to me pppoe@139.com

> 做完效果怎么样  (这是电脑版，手机版后面做)
<img src="https://github.com/charlesld/IAMAWIFIEXPERT/blob/master/pic/aliguest_wifi_pc.jpg" width=500 height=250 />

[代码位置](guest_wifi/aliguest/gw/ce.py)


## wifi sniffer

抓包，替monitor环境做准备，拉取了珍藏已久的抓包网卡和软件。
  
安利一下Motorola Airdefense Mobile。东西是好东西，知道的人不多，在中国用到的人寥寥无几。

>  抓包，设定filter 和别名，获取连接关系

![01](/pic/cap01.jpg)

> 交互式获取报文信息

![02](/pic/cap02.jpg)

> 查看报文详情

![03](/pic/cap03.jpg)

> 获取空口环境的一些信息

![04](/pic/cap04.jpg)


