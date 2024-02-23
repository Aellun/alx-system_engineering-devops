# This script enables the user Holberton to log in and change files

# Increase hard file limit for user holberton
exec { 'increase_hard_file_limit_for_holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for user holberton
exec { 'increase_soft_file_limit_for_holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
