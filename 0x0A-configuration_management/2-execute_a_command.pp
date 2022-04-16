# Kills specific process killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
