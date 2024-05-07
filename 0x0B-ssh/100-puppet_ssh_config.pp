# Update SSH config file
file { '/etc/ssh/ssh_config':
  ensure => file,
  content => 'Host * BatchMode yes IdentityFile ~/.ssh/school'
}
