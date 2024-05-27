# Script to install and config nginx with puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'index':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'reload':
  command  => 'sudo service nginx reload',
  provider => shell,
}
