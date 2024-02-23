# This script increase the amount of request the nginx server can handle

# Increase ULIMIT for the default file
exec { 'adjust_ulimit_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
-> exec { 'restart_nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
