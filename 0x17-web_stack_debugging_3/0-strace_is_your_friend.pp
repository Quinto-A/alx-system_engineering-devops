exec { 'fix-apache-permissions':
    command => 'chown -R www-data:www-data /var/www/html',
    path    => ['/bin', '/usr/bin'],
}
