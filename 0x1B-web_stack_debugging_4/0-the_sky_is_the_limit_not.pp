# resolving our web server trafic on presure

exec {'replace':
  source  => shell,
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before  => Exec['restart'],
}

exec {'restart':
  source  => shell,
  command => 'sudo service nginx restart',
}
