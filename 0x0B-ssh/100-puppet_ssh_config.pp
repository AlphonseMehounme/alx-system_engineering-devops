# Update SSH config file
file { '~/ssh/config':
  ensure => file,
  content => 'Host * BatchMode yes IdentityFile ~/.ssh/school'
}
