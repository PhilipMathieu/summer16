#!/usr/bin/expect
#This script turns on or off an argument-specified port on the Synaccess power 
#strip. It checks first to see if the port is already in the correct state.  
#This is not strictly necessary, but it was good practice for a future scripts 
#that might want to monitor and parse status strings. It uses Expect,
#a package that facilitates automation of terminal and TCP-style interfaces
#Initiate telnet connection
lassign $argv portnum onoff
spawn telnet 192.168.1.100
expect ">"
#Login
send "\$A1 admin admin\r"
expect "\$A0"
#get port statuses
send "\$A5\r"
expect -re "(\[0-9]\{6})"
set status $expect_out(0,string)
set status [string range $status [expr 6-$portnum] [expr 6-$portnum]]
if {$status ne $onoff} {
send "\$A3 $portnum $onoff \r"
expect "\$A0"
}
#Exit
send "\035"
expect "telnet>"
send "close"
