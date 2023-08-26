# Execute a command to kill a process named killmenow

# Execute the pkill command to terminate the process
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  onlyif      => 'pgrep -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

# Notify to print "OK" when the process is successfully terminated
notify { 'OK':
  subscribe => Exec['killmenow'],
}
