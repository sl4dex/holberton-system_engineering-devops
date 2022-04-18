exec { 'kill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/:',
}
