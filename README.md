# About

Pulls ipdb results from https://www.abuseipdb.com using the [api](https://docs.abuseipdb.com/#introduction).

# Prerequisites

Sign up on abuseipdb and generate an API key, the script relies on this being assigned to the environmental variable "ABUSE_API_KEY".

# Use

## General use

`python abusecheck.py 192.168.0.1`<br>
`====================================================`<br>

`Results for 192.168.0.1`<br>
`===`<br>
`Private IP`<br>
`Country: None`<br>
`Owner: None`<br>
`Abuse confidence: 0 %`<br>
`Times reported: 86`<br>

`====================================================`<br>

## Optional output

If an IP is private <br>
`This is a Private address`<br><br>

If an IP has been reported: <br>
`iptables -I INPUT -s <IP> -j DROP`<br>
