# Installing Nginx with puppet
package { 'nginx':
  ensure => installed,
}

file_line { 'Aaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://vidmate.en.softonic.com/download permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
  enable  => true,
}
