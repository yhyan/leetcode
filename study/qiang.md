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

shadowsocks 源码可以查看 [这里](http://lxr.yanyahua.com/source/shadowsocks)

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

# shadowsocks-qt5 安装

wiki: https://github.com/shadowsocks/shadowsocks-qt5/wiki

shadowsocks-qt5 需要通过PPA源安装，仅支持Ubuntu 14.04或更高版本。

1. 设置 PPA 源并安装 shadowsocks-qt5

```
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

2. 安装过程如果遇到 libappindicator1 依赖问题（dependency problems），而 libappindicator1 又遇到 libindicator7 依赖的解决办法。一并安装 libappindicator1 libindicator7 依赖，再重新安装 shadowsocks-qt5。

```
sudo apt-get -f install libappindicator1 libindicator7
```

3. 完成后就可以打开 shadowsocks-qt5 啦

注意，ss-qt5 和 supervisor 安装的方式只使用一种就可以了。

如要要两种都使用，可以将Port改为不一样，例如一个是1080，一个是1090。


# ubuntu 全局配置代理

1. 安装GenPAC

GenPAC 是基于gfwlist的代理自动配置（Proxy Auto-config）文件生成工具，支持自定义规则。

```
sudo pip install genpac
pip install --upgrade genpac
```

2. 下载gfwlist

```
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" --gfwlist-url=https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt --output="autoproxy.pac"
```

3. 设置全局代理

点击：System settings > Network > Network Proxy，选择 Method 为 Automatic，设置 Configuration URL 为 autoproxy.pac 文件的路径，点击 Apply System Wide。 格式如：file:///home/XX/autoproxy.pac

这个时候会出现google浏览器无法访问google.com，但是firefox可以访问。

并不是全局代理的设置没有生效，而是 Chrome移除对file://和data:协议的支持，目前只能使用http://协议。

因此，我们打算使用nginx实现对本地文件的http映射。

4. 安装nginx

```
sudo apt-get install nginx
```

修改nginx.cnf配置文件

vim /etc/nginx/nginx.conf

```
server{
    listen 80; #注意这里不用":"隔开，listen后面没有冒号
    server_name 127.0.0.1; #注意这里不用":"隔开，server_name后面没有冒号
    location /autoproxy.pac {
        alias 绝对路径/autoproxy.pac;
    }
}
```

重启nginx

```
sudo nginx -s reload
```

最后一步

把http://127.0.0.1/autoproxy.pac填写到上述操作的url中
