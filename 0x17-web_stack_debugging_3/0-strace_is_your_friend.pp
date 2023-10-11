# Puppet manifest to fix Apache 500 error

# Define an exec resource to fix the issue
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/'
}
