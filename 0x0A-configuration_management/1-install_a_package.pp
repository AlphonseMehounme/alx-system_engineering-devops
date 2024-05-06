# Install flask 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider => 'pip3'
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
