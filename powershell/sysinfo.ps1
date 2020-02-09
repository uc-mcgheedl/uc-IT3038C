function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}


$IP = getIP

write-host("This machines IP is $IP")
