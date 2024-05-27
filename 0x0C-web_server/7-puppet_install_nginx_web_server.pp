# Script to install and config nginx with puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => 'shell',
}

exec {'index':
  command  => 'echo "hello world" | sudo tee /var/www/html/index.html',
  provider => 'shell',
}

exec {'config':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec {'reload':
  command  => 'service gninx restart; service gninx reload',
  provider => 'shell',
}

#exec {'config':
#  commande => 'printf %s "server {
#        listen 80 default_server;
#        listen [::]:80 default_server;
#        root /var/www/html;
#        index index.html index.htm index.nginx-debian.html;
#        location /redirect_me {
#                return 301 https://www.google.com;
#        }
#}" > /etc/nginx/sites-available/default',
