# This resolve the ammount of user active

exec {'replace-1':
  source  => shell,
  command => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before  => Exec['replace-2'],
}

exec {'replace-2':
  source  => shell,
  command => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
