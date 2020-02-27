# Use

## General use

[root@testbox abuseipdb-cli]# ipdb 192.168.0.1<br>

====================================================<br>

Results for 192.168.0.1<br>
===<br>
Private IP<br>
Country: None<br>
Owner: None<br>
Abuse confidence: 0 %<br>
Times reported: 86<br>

====================================================<br>


## Optional output

If an IP is private <br>
`This is a Private address`<br><br>

If an IP has been reported: <br>
`iptables -A INPUT -s <IP> -j DROP`<br>
