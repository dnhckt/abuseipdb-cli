# About

Command line tool to pull ipdb results from https://www.abuseipdb.com using the [API](https://docs.abuseipdb.com/#introduction).

# Prerequisites

* Sign up on abuseipdb and generate an API key<br>
* Assign your API KEY to the environmental variable "ABUSE_API_KEY" (or run install.sh).

# Install

`wget https://raw.githubusercontent.com/dnhckt/abuseipdb-cli/master/abusecheck.sh` 
<br>
`chmod +x abusecheck.sh`
<br>
`./abusecheck <IP>` 

## Optional, but recommended

Must be ran in the same directory as the abusecheck.sh file.

`wget https://raw.githubusercontent.com/dnhckt/abuseipdb-cli/master/install.sh` 
<br>
`chmod +x install.sh` 
<br>
`./install.sh` 
<br>
` Enter your API key: (paste and enter)` 

# Example use 

`ipdb 192.168.0.1`<br>
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
