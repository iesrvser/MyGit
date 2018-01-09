
系统启动时默认进入命令行
'systemctl set-default multi-user.target'

系统启动时默认进入图形界面
'systemctl set-default graphical.target'

命令行中启动图形界面
'sudo systemctl start lightdm.service'

临时更改APT代理设置
'sudo apt-get -o Acquire::http::proxy="http://127.0.0.1:8000/" update'

永久更改APT代理设置
'sudo nano /etc/apt/apt.conf' 没有apt.conf文件就创建一个
'Acquire::http::Proxy “http://proxyusr:password@yourproxyaddress:proxyport”';  
'Acquire::https::Proxy “https://proxyusr:password@yourproxyaddress:proxyport”';

