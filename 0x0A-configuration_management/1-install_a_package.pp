# This ensure that version 2.1.0 Flast is installed.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}

package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}
