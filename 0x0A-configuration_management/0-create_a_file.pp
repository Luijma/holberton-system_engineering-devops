# Creating a file in /tmp for task 0

file { school:
		ensure => file,
		path => '/tmp/school',
		mode => '0744'
		owner => 'www-data',
		group => 'www-data',
		content => 'I love Puppet',

}
