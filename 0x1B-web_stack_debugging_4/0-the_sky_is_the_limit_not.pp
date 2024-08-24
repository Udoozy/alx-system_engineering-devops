# resolving our web server trafic on presure

exec { 'limit_replace':
  command => 'sed -i "s/15/5000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
