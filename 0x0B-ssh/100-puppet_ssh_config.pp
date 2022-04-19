# creates config file for ssh client

$str = "Host 34.74.207.217
  IdentityFile ~/.ssh/school

PasswordAuthentication no
"

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $str,
}
