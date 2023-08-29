# Define the main class
class web_server {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('web_server/nginx_config.erb'),
    require => Package['nginx'],
  }
}

# Define the redirect class
class web_server::redirect {
  file { '/etc/nginx/sites-available/redirect_me':
    ensure  => file,
    content => template('web_server/redirect_config.erb'),
    require => Package['nginx'],
  }

  file { '/var/www/html/redirect_me':
    ensure  => directory,
    require => File['/etc/nginx/sites-available/redirect_me'],
  }

  file { '/var/www/html/redirect_me/index.html':
    ensure  => file,
    content => 'Redirecting...',
    require => File['/var/www/html/redirect_me'],
  }
}

# Include both classes in the node definition
node 'default' {
  include web_server
  include web_server::redirect
}
