# This resolve the ammount of user active

exec {'update_config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin:/usr/sbin',
}
