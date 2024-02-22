# This script enables the user Holberton to logina and change files

# Increase hard file limit for user holberton
file_line { 'increase-hard-file-limit-for-holberton-user':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 50000',
  match   => 'holberton hard nofile',
  ensure  => present,
}

# Increase soft file limit for user holberton
file_line { 'increase-soft-file-limit-for-holberton-user':
  path    => '/etc/security/limits.conf',
  line    => 'holberton soft nofile 50000',
  match   => 'holberton soft nofile',
  ensure  => present,
}
