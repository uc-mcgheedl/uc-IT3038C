function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

$IP = getIP
$myname = hostname
$tdy = date

$BODY = "This machines IP is $IP.User is Administrator .Hostname is $myname. Powershell Version is 5.Today's date is $tdy."
write-host ("$BODY")
Send-MailMessage -To "mcgheedl@mail.uc.edu" -From "me@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

Write-Host ("Email Sent!")

