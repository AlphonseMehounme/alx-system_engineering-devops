# Update SSH config file
file { "Turn off passwd auth":
  name   => '/etc/ssh/ssh_config',
  path   => '/etc/ssh/ssh_config',
  line   => "BatchMode yes",
  ensure => present
}
