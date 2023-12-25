# Define a package resource for Python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}

# Define a package resource for Flask with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3.8'],
}

# Define a package resource for Werkzeug with version 2.1.1
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}

# Notify the user when the packages are installed
notify { 'Packages installed':
  require => Package['Werkzeug'],
}
