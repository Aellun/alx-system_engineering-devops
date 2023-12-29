#!/usr/bin/env bash
#using puppet to carryout client configuration
file { '/etc/ssh/ssh_config':
  ensure  => present,
}
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'passwordAuthentication no',
  match => '^#passwordAuthentication',
}
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'identyFile ~/.ssh/school',
  match => '^#identyFile',
}
