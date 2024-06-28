# This ensure that version 2.1.0 Flast is installed.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
