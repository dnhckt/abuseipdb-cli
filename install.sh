#! /bin/bash -i

cp abusecheck.sh /usr/local/bin/abusecheck
chmod +x /usr/local/bin/abusecheck

read -p "Enter your API key:" apikey
export ABUSE_API_KEY="$apikey"
