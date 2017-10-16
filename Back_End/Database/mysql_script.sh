#!/bin/sh
# test mysql script

mysql -uroot -proot <<EOF

show databases;

use test; 

select * from instructor;

EOF

echo "This is a test of script on mysql"

# A simple way to use shell script, however it's not secure to show our password on script
# there is another better way to hide our password
