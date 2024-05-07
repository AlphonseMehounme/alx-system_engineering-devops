# Update SSH config file
file { '/etc/ssh/ssh_config':
  ensure => file,
  content => "Host *\n  PubkeyAuthentication yes\n  IdentityFile ~/.ssh/school\n"
}
