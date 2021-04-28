# mac git ssh

[https://stackoverflow.com/questions/62986397/ssh-config-file-for-git-on-mac-timeout](https://stackoverflow.com/questions/62986397/ssh-config-file-for-git-on-mac-timeout)

[https://stackoverflow.com/questions/35558649/github-error-ssh-connect-to-host-github-com-port-22-operation-timed-out-fat](https://stackoverflow.com/questions/35558649/github-error-ssh-connect-to-host-github-com-port-22-operation-timed-out-fat)



最简单的解决办法

编辑 ~/.ssh/config 文件：

```
Host github.com
  Hostname ssh.github.com
  Port 443

```

[https://docs.github.com/en/github/authenticating-to-github/using-ssh-over-the-https-port](https://docs.github.com/en/github/authenticating-to-github/using-ssh-over-the-https-port)

[https://gist.github.com/Tamal/1cc77f88ef3e900aeae65f0e5e504794](https://gist.github.com/Tamal/1cc77f88ef3e900aeae65f0e5e504794)

