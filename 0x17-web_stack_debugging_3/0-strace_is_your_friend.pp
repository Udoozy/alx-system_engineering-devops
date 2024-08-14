# This is used to find out why Apache is returning a 500 error

file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html'],
}

# Fix a known issue in the WordPress configuration file
exec { 'fix-wordpress-config':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}
