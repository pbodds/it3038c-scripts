##Get-service | format-list displayname, status
#Get-service | format-table displayname, status
#Get-Service | Format-Table *
#Get-Service | Sort-Object -Property Status -Descending | Format-Table displayname, status
#get-service | Sort-Object -Property Status -Descending | Format-Table displayname, status |  Out-File -FilePath C:\services.txt 
#Remove-Item C:\services.txt

#Get-Service | Out-GridView
#Get-Service | Select-Object displayname, status | Out-GridView
#Get-Service | Select-Object * | Out-GridView

#$Hello = "Hello, PowerShell"
#Write-Host($Hello)


Function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

Write-Host(getIP)

$IP = getIP
Write-Host("This machine's IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)
