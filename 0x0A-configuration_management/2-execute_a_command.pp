# Use exec to kill a process
exec { 'killmenow':
  command   => "pkill -f killmenow"
  path      => "./killmenow"
}
