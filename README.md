# About
CLI tool to check if an IP is reported as malicious 
# Install

# Use
`ipdb 123.123.123.123
##########
Results for 123.123.123.123
===
This IP seems to be from CN and is owned by chinaunicom.com
There is 0 % confidence this is abusive. Previously reported 2 times
`
If an IP starts with 192 / 172:
`
Is this IP Public?: False
`
If an IP has been reported: 
`
iptables -A INPUT -s <IP> -j DROP
`
