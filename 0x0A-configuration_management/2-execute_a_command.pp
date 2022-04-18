# kills the process killmenow
exec { 'kill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/:',
}
