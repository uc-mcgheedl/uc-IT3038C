#:/bin/bash
emailaddress=mcgheedl@mail.uc.edu
echo Hostname: $HOSTNAME 
a=$(ip a | grep 'dynamic ens192'| awk '{print $2}') 
echo IP IS $a
tdy=$(date +"%d-%m-%Y") 
echo Today is: $tdy

printf "The Server name is $HOSTNAME %s\nThe IP is :$a, %s\nToday is $tdy, %s\nBash Version is $BASH_VERSION" | mail -s "IT3038C Linux IP" $emailaddress 

