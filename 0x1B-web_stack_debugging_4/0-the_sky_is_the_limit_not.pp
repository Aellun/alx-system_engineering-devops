# This script increase the amount of request the nginx server can handle

# Manage nginx configuration file
file { '/etc/default/nginx':
  ensure  => file,
  content => template('your_module/nginx_config.erb'),
  notify  => Exec['nginx-restart'],
}

# Exec resource to restart Nginx
exec { 'nginx-restart':
  command     => 'systemctl restart nginx',
  refreshonly => true,
  path        => ['/bin', '/usr/bin'],
}

# Modify max open files limit using sed
exec { 'modify-max-open-files-limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/bin:/usr/bin', # Adjust the path as needed
  notify  => Exec['nginx-restart'],
}
