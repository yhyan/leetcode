# ubuntu desktop 16.04 访问外网


### 安装ss client

```
$ apt-get install shadowsocks
$ sslocal -s server_address -p server_port -k password -m method

```

查看 shadowsocks deb 的文件内容：

```
$ mkdir /tmp/ss
$ cd /tmp/ss
$ cp /var/cache/apt/archives/shadowsocks_2.1.0-1_all.deb .
$ dpkg -L shadowsocks
```

可以看到，实际上就是 [shadowsocks python代码](https://github.com/shadowsocks/shadowsocks/tree/master)



### 安装 anaconda.sh

### 安装supervisor

### 在supervisor中配置 sslocal 开机启动

```
/etc/supervisor/conf.d$ cat shadowsocks.conf
[program:shadowsocks]
command=/usr/bin/sslocal -c /home/XX/shadowsocks.json
autostart=true
autorestart=true
user=XX
log_stderr=true
logfile=/tmp/supervisord_shadowsocks.log

```



### 安装firefox插件

打开Firefox浏览器，输入about:addons，进入插件安装页面。

搜索Proxy SwitchyOmega，安装它。

在Proxy SwitchyOmega的属性页面，新建profile，填写以下内容：

```
Protocol: SOCK5
Server: 127.0.0.1
Port: 1080
```

然后将此profile命名，如ss。

在Firefox的工具栏，点击代表SwitchyOmega的小圆圈，选择ss。


# git 配置proxy

```
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```

