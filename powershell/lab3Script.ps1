Set-ExecutionPolicy -ExecutionPolicy Unrestricted
Function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

Function getUser{
(Get-LocalUser) | Select-String "Admin*"
}

Function getHostName{
(Get-ComputerInfo).CsDNSHostName
}

Function getVersion{
(Get-Host).Version.Major
}

$IP = getIP
$USER = getUser
$HostName = getHostName
$VERSION = getVersion
$DATE = Get-Date

write-host(getIP)
write-host(getUser)
write-host(getHostName)
write-host(getVersion)

#Write-Host("This machine's IP is $IP")
#Write-Host("Today's date is {0:dddd, MMMM dd, yyyy}" -f (Get-Date))
#Write-Host("Powershell Version {0}"-f (Get-Host).Version.Major)
#Write-host("This machine's IP is $IP. The User is $env:USERNAME. Hostname is $env:USERDOMAIN. Powershell Version {0}"-f (Get-Host).Version.Major + ". Today's date is {0:dddd, MMMM dd, yyyy}" -f (Get-Date))
#Write-output("This machine's IP is $IP. The User is $env:USERNAME. Hostname is $env:USERDOMAIN. Powershell Version {0}"-f (Get-Host).Version.Major + ". Today's date is {0:dddd, MMMM dd, yyyy}" -f (Get-Date)) | Out-File -FilePath C:\SystemInformation.txt 


$From = "pmvboddy@gmail.com"
$To = "reedws@ucmail.uc.edu"
$Attachment = "C:\SystemInformation.txt"
$Subject = "IT3038C Windows SysInfo"
$Body = ("This machine's IP address is $IP. The user is $USER. The HostName is $HostName. The version is $VERSION. The date is $DATE.") 
#$Body =Write-host("This machine's IP is $IP. The User is $env:USERNAME. Hostname is $env:USERDOMAIN. Powershell Version {0}"-f (Get-Host).Version.Major + ". Today's date is {0:dddd, MMMM dd, yyyy}" -f (Get-Date)) 
$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"

Send-MailMessage -From $From -to $To -Subject $Subject -Body $Body -SmtpServer $SMTPServer -Port $SMTPPort -UseSsl -Credential (Get-Credential) -Attachments $Attachment





#I GIVE UP! "Cannot validate argument on parameter 'Body'. The argument is null or empty. Provide an argument that is not null or empty, and then try the command again." Can't figure this out. 


## Broken body. $Body = write-host("This machine's IP address is $IP. The user is $USER. The HostName is $HOST. The version is $VERSION. The date is $DATE.") 
#$Body = write-host("This machine's IP address is $IP. The user is $USER. The HostName is $HOST. The version is $VERSION. The date is $DATE.") 