# Use exec to kill a process
exec { 'Process killer'
  command   => "pkill 'killmenow'"
}
