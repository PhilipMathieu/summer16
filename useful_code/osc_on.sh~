#!/usr/bin/expect
#This script turns on all outlets on the Synaccess power strip. It uses Expect,
#a package that facilitates automation of terminal and TCP-style interfaces
#Initiate telnet connection
spawn telnet 192.168.1.100
expect ">"
#Login
send "\$A1 admin admin\r"
expect "\$A0"
#Power all on
send "\$A7 1\r"
expect "\$A0"
#Exit
send "\035"
expect "telnet>"
send "close"
