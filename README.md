# About
CLI tool to check if an IP is reported as malicious 
# Install

# Use

## General use

`ipdb 123.123.123.123`<br>

`##########`<br>
`Results for 123.123.123.123`<br>
`===`<br>
`This IP seems to be from CN and is owned by chinaunicom.com`<br>
`There is 0 % confidence this is abusive. Previously reported 2 times`<br>

## Optional parameters

If an IP starts with 192 / 172:<br>
`Is this IP Public?: False`<br>
If an IP has been reported: <br>
`iptables -A INPUT -s <IP> -j DROP`<br>
