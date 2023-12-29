#!/usr/bin/env puppet
#using puppet to configure no password access to server

file { '/etc/ssh/ssh_config':
  ensure => present,
}

ssh_config { 'Turn off password auth':
  path  => '/etc/ssh/ssh_config',
  value => 'PasswordAuthentication no',
}

ssh_config { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  value => 'IdentityFile ~/.ssh/school',
}
