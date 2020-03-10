$RANDO=0
for($i=0; $i -lt 5; $i++){
    $RANDO=Get-Random -Maximum 1000 -Minimum 1
    write-host($RANDO)
}