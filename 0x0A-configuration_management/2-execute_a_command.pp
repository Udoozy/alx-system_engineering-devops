# This uses the pkill comman to kill killmenow process.

exec { 'kill killmenow process':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
