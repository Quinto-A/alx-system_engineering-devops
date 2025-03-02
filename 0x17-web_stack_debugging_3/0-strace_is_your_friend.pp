#fixes apache 500 error
exec { 'fix-apache-permissions':
    command => 'chown -R www-data:www-data /var/www/html',
    path    => ['/bin', '/usr/bin'],
}
