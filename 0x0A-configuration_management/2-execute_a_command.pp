# Use exec to kill a process
exec { 'killmenow':
  command   => '/usr/bin/pkill -f killmenow'
}
