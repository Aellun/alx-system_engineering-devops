# Setting up New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}
# Install Nginx package
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}
# Enable the default and redirect_me sites
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}
# Ensure Nginx is running
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
