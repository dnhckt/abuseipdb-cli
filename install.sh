#! /bin/bash -i

cp abusecheck.sh /usr/local/bin/ipdb
chmod +x /usr/local/bin/ipdb

read -p "Enter your API key:" apikey
export ABUSE_API_KEY="$apikey"
