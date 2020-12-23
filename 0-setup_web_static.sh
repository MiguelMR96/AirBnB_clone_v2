#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases/test
sudo echo "
<html>
<head></head>
<body>
<p>Test for web server nginx to deploy</p>
</body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
